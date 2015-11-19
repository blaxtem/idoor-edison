#!/usr/bin/python
# https://github.com/SavinaRoja/PyUserInput

from wiringx86 import GPIOEdison as GPIO
gpio = GPIO(debug=False)
pinButtons = [2,3,4]
state = [0,0,0]
for i in pinButtons:
	gpio.pinMode(i, gpio.INPUT)
while True:
	for i in range(3):
		state[i] = gpio.digitalRead(pinButtons[i])
		if state[i] == 1:
                        print "Boton en pin " + str(pinButtons[i]) + " pulsado."

