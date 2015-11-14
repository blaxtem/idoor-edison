#!/usr/bin/python

import os, sys, time                             
sys.path.insert(1, os.path.split(sys.path[0])[0])
                                                                           
import re                                                                  
import time                                                                
import errno
import argparse                                  
import logging                                   
logging.basicConfig(format='%(relativeCreated)d ms [%(name)s] %(message)s')
                                                                           
import nfc                                                                 
import nfc.clf                                                             
import urllib2

class NFC():
	def read(self,web):
		clf = nfc.ContactlessFrontend("usb")                                       
		target1 = nfc.clf.RemoteTarget("106A")          
		str = str(clf.sense(target1, iterations=20, interval=0.4))
		str2 = str[13:21]                                                         
		response = urllib2.urlopen(web+str2)
	      	clf.close()
		return response
