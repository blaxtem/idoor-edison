#!/usr/bin/env python

#TODO Metodo de parsing

import os, NFC, menu, thread, buttons, sys, curses, npyscreen

# Control de errores en los argumentos
if len(sys.argv) <= 1:
	print "Usage: python controller.py <delay_of_button_read> <web>"

class Controller:
	def parsing(self,response):
		return None
	def run(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		print "Acerque la targeta de la universidad al lector de la derecha."
		nfc = NFC.NFC()
		# Bucle hasta la lectura de una targeta
		while True:
			response = nfc.read(sys.argv[2])
			if response != None: 
				break;
		self.datos = parsing(response)
		# Inicializacion del entorno grafico 
		menu = menu2()
	
	# Vuelta al estado inicial
	def stop(self):
		run()
if __name__ == "__main__":
    ctrl = Controller()
    try:
	# Creacion del thread encargado de leer los pins de los botones
    	bd = thread.start_new_thread( buttons_daemon, ("Buttons", sys.argv[1]) )
    except:
    	print "Error: unable to start the button daemon"
    ctrl.run()
