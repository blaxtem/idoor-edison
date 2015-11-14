#!/usr/bin/python
# https://github.com/SavinaRoja/PyUserInput

import thread, time
from pymouse import PyMouse
from wiringx86 import GPIOEdison as GPIO

def buttons_daemon (thread_name, delay):
	gpio = GPIO(debug=False)
	pinButtons = [2,3,4]
	state = [0,0,0]
	k = PyKeyboard()
	for i in pinButtons:
		gpio.pinMode(i, gpio.INPUT) 
	while True:
		for i in xrange(3):
			state[i] = gpio.digitalRead(pinButtons[i])
		if state[1] == 1 and state[2] == 0 and state[3] == 0: #Up Arrow
			k.tap_key('up')	
		if state[2] == 1 and state[1] == 0 and state[3] == 0: #Down Arrow (tab)
			k.tap_key('tab')
		if state[3] == 1 and state[1] == 0 and state[2] == 0: #OK (enter)
			k.tap_key('enter')
		#if state[]
		time.sleep(delay)
