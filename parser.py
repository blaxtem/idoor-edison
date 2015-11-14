#!/usr/bin/env python

import re

class parser:
	def __init__(self, response):
		self.datos = response.read()
		groupCreation()
	def nextClass(self):
		
	def lastGrade(self):
		
	def lastAssignment(self):
		
	def gridCreation(self,gd):
		gd.values = []
        horas = [8,9,10,11,12,13,14,15,16,17,18,19,20]
        for z in range(len(horas)):
             for x in range(2):
             	row = []
             for y in range(6):
                if y == 0:
    	            row.append(horas[z])
                elif bool(random.getrandbits(1)):
                    row.append("CLASE")
                else:
                    row.append("NO CLASE")
    	     gd.values.append(row)	
	def groupCreation(self):
		m = re.match(, self.datos)