#!/usr/bin/python

import nfc
import nfc.clf
#import urllib2
import sys, os
#web = 'http://raiblax.com/pbe/receptor.php?id_alumno=FB68CCF1'
clf = nfc.ContactlessFrontend("usb")
target1 = nfc.clf.RemoteTarget("106A")
str = str(clf.sense(target1, iterations=20, interval=0.4))[13:21]
print "Tu id es " + str
