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


Install
-------

Right now this is a simple python script.

```sh
git clone git@github.com:jchook/too-loud.git
cd too-loud
pip install -r requirements.txt
```


Usage
-----

```sh
python main.py
```

Modify the variables inside the main.py script to adjust the sensitivity and the alert sound.


License
-------

MIT.
