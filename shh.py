import pyaudio
import time
from math import log10
import audioop
from pydub import AudioSegment
from pydub.playback import play
import os
import platform

# Threshold settings
ALERT_FREQUENCY = float(os.environ.get('SHH_ALERT_FREQUENCY', '1'))  # Time in seconds between alerts
ALERT_MESSAGE = os.environ.get('SHH_ALERT_MESSAGE', 'Please be quiet, you are too loud!')
ALERT_SOUND = os.environ.get('SHH_ALERT_SOUND', 'alert.wav') # Must be wav file
DECIBEL_THRESHOLD = float(os.environ.get('SHH_DECIBEL_THRESHOLD', '-30.0'))  # Adjust this to set the sensitivity in dB
SENSITIVITY = float(os.environ.get('SHH_SENSITIVITY', '0.8'))  # 0.0 (pure RMS) to 1.0 (pure Peak)

# Initialize PyAudio
p = pyaudio.PyAudio()
WIDTH = 2
RATE = int(p.get_default_input_device_info()['defaultSampleRate'])
DEVICE = int(p.get_default_input_device_info()['index'])
hybrid_metric = 0.0000001

def play_alert():
    play(alert_sound)

def send_system_notification():
    system = platform.system()
    if system == 'Windows':
        os.system(f"msg * \"{ALERT_MESSAGE}\"")
    elif system == 'Darwin': # macOS
        os.system(f"osascript -e 'display notification \"{ALERT_MESSAGE}\" with title \"Shh\"'")
    elif system == 'Linux':
        os.system(f"notify-send '{ALERT_MESSAGE}'")

def callback(in_data, frame_count, time_info, status):
    global hybrid_metric
    rms = audioop.rms(in_data, WIDTH) / 32767  # RMS amplitude
    peak = audioop.max(in_data, WIDTH) / 32767  # Peak amplitude

    # Create hybrid metric using sensitivity
    hybrid_metric = (1 - SENSITIVITY) * rms + SENSITIVITY * peak
    return in_data, pyaudio.paContinue

# Load the sound file once
alert_sound = AudioSegment.from_file(ALERT_SOUND)

# Open the stream
stream = p.open(format=p.get_format_from_width(WIDTH),
                input_device_index=DEVICE,
                channels=1,
                rate=RATE,
                input=True,
                output=False,
                stream_callback=callback)

stream.start_stream()
last_alert_time = 0

try:
    while stream.is_active():
        db = 20 * log10(hybrid_metric)
        # print(f"Hybrid Metric: {hybrid_metric} DB: {db}")

        # Check if the decibel level exceeds the threshold
        if db > DECIBEL_THRESHOLD and (time.time() - last_alert_time) > ALERT_FREQUENCY:
            play_alert()
            send_system_notification()
            last_alert_time = time.time()

        # Refresh every 0.1 seconds for quicker detection
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Monitoring stopped")

finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
