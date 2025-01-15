Too Loud
========

*SHH!* Receive audio alerts on your computer when you are being too loud.


About
-----

For night owls or morning larks, it's easy to get carried away and get a little loud while others in your household are trying to get their much needed rest.

This app monitors the microphone input on your computer and plays a "SHH!" sound when you exceed a certain decibel threshold.


Features
--------

- [x] Adjustable decibel sensitivity
- [x] Adjustable peak sensitivity
- [x] Custom alert sounds

Download
--------

Download the application from the [Releases](https://github.com/jchook/too-loud/releases) section.


Environment Variables
---------------------

| Variable | Default | Description |
|----------|---------|-------------|
| `SHH_ALERT_FREQUENCY` | 1 | Time in seconds between alerts |
| `SHH_ALERT_MESSAGE` | Please be quiet... | Alert message to show |
| `SHH_ALERT_SOUND` | alert.wav | Must be wav file |
| `SHH_DECIBEL_THRESHOLD` | -30.0 | dB threshold for an alert |
| `SHH_SENSITIVITY` | 0.8 | Between 0 and 1, sensitivity to volume spikes |


Development
-----------

To modify too-loud, clone it and install the python requirements.

```sh
git clone git@github.com:jchook/too-loud.git
cd too-loud
pip install -r requirements.txt
```


License
-------

MIT.
