#!/usr/bin/python
# https://github.com/SavinaRoja/PyUserInput

import thread, time
from pymouse import PyMouse
from wiringx86 import GPIOEdison as GPIO

def buttons_daemon (thread_name, delay):
	# Inicializacion de los pins GPIO
	gpio = GPIO(debug=False)
	pinButtons = [2,3,4]
	state = [0,0,0]
	# Creacion del objecto que simula los eventos de teclado
	k = PyKeyboard()
	for i in pinButtons:
		# Configuracion a modo Input de todos los pins que usaremos
		gpio.pinMode(i, gpio.INPUT) 
	while True:
		for i in xrange(3):
			state[i] = gpio.digitalRead(pinButtons[i])
		if state[0] == 1 and state[1] == 0 and state[2] == 0: #tab
			k.tap_key('tab')	
		if state[1] == 1 and state[0] == 0 and state [2] == 0: #Up
			k.tap_key('right')
		if state[2] == 1 and state[0] == 0 and state[1] == 0: #OK
			k.tap_key('enter')
		time.sleep(delay)
