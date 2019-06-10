############################################################################################################################################
#agsm2_b-gsmgnss_105_hw_control.py v1.01/24 March 2017 - a-gsmII/b-gsmgnss 2.105 HARDWARE CONTROL library 
#COPYRIGHT (c) 2017 Dragos Iosub / R&D Software Solutions srl
#
#You are legaly entitled to use this SOFTWARE ONLY IN CONJUNCTION WITH a-gsmII or b-gsmgnss DEVICES USAGE. Modifications, derivates and redistribution 
#of this software must include unmodified this COPYRIGHT NOTICE. You can redistribute this SOFTWARE and/or modify it under the terms 
#of this COPYRIGHT NOTICE. Any other usage may be permited only after written notice of Dragos Iosub / R&D Software Solutions srl.
#
#This SOFTWARE is distributed is provide "AS IS" in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied 
#warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
#Dragos Iosub, Bucharest 2017.
#https://itbrainpower.net
############################################################################################################################################
#HEALTH AND SAFETY WARNING!!!!!!!!!!!!!!!!!!!!
#High power audio (around 870mW a-gsmII, 800mW b-gsmgnss)! You can damage your years! Use it with care when headset is connected.
#We recomend to use AT+CLVL=20 (as maximum value), audio setup command in order to limit the output power.
#
# WARNING: WIRING the gsm board with u-controllers/boards(RPi) must be made with boards UNPOWERED!!
#
# LEGAL DISCLAIMER:
# Incorrect or faulty wiring and/or connection can damage your RPi and/or your a-gsm board!
# Following directives are provided "AS IS" in the hope that it will be useful, but WITHOUT ANY WARRANTY!
# Do the wiring on your own risk! 
#
# References:
# https://itbrainpower.net/images/RaspberryPi_a-gsmII_b-gsmgnss_wiring.png
# https://itbrainpower.net/downloads#a-gsmII_documentation
# https://itbrainpower.net/downloads#b-gsmgnss_documentation
############################################################################################################################################

import os
import RPi.GPIO as GPIO
from globalParVar import *
from time import sleep
from agsm_Serial_Lib import *

# getModemState()
# returns 1 if the modem is up, 0 else
def getModemState():
        return GPIO.input(STATUS)

# getModemStateByAT()
# returns 1 if the modem is running, 0 else
# can be used as substitute for getModemState()
def getModemStateByAT():
        aGsmWRITE("+++\r\n")
        aGsmWRITE(chr(0x1B)+"\r\n")
        aGsmWRITE("AT\r\n")
        aGsmWRITE("ATE1\r\n")
        aGsmWRITE("ATV1\r\n")
        clearSInput()
        clearInput()
        res = sendATcommand("AT",["OK","ERROR"],1)
        if(res>0):
                return 1
        else:
                return 0

def poweron():
	if not(getModemState()):
		print ("try to wake a-gsmII/b-gsmgnss")
		#GPIO.output(POWER,GPIO.HIGH) #a-gsm 2.064
		GPIO.output(POWER,GPIO.LOW)
		sleep(1)
		#GPIO.output(POWER,GPIO.LOW) #a-gsm 2.064
		GPIO.output(POWER,GPIO.HIGH)
	sleep(5)	
	if (getModemState()):
		print("a-gsmII/b-gsmgnss is up")
	else:
		print("failure powering a-gsmII/b-gsmgnss")
		exit(100)
	
def poweroff():
	#if GPIO.input(STATUS):
	if (getModemState()):
		print ("try to shutdown a-gsmII/b-gsmgnss")
		#GPIO.output(POWER,GPIO.HIGH) #a-gsm 2.064
		GPIO.output(POWER,GPIO.LOW)
		sleep(1)
		#GPIO.output(POWER,GPIO.LOW) #a-gsm 2.064
		GPIO.output(POWER,GPIO.HIGH)
	sleep(8)
	#if not GPIO.input(STATUS):
	if not(getModemState()):
		print("a-gsmII/b-gsmgnss is down")
	else:
		print("failure powering off a-gsmII/b-gsmgnss")
		exit(100)

def restartModem():
    poweroff()
    sleep(3)
    poweron()

def resetModem():
	print ("try to reset a-gsmII/b-gsmgnss")
	#GPIO.output(RESET,GPIO.HIGH) #a-gsm 2.064
	GPIO.output(RESET,GPIO.LOW)
	sleep(1)
	#GPIO.output(RESET,GPIO.HIGH) #a-gsm 2.064
	GPIO.output(RESET,GPIO.HIGH)
	sleep(8)
	#if not GPIO.input(STATUS):
	if not(getModemState()):
		print("a-gsmII/b-gsmgnss is down")
	else:
		print("failure reset a-gsmII/b-gsmgnss")
		exit(100)

def hwControlSetup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    try:
        GPIO.setup(STATUS, GPIO.IN)
	#GPIO.setup(POWER, GPIO.OUT, initial=GPIO.HIGH) #a-gsm 2.064
	#GPIO.setup(RESET, GPIO.OUT, initial=GPIO.HIGH) #a-gsm 2.064
        GPIO.setup(POWER, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(RESET, GPIO.OUT, initial=GPIO.HIGH)
    except:
        GPIO.cleanup()#free GPIO
        GPIO.setup(STATUS, GPIO.IN)
	#GPIO.setup(POWER, GPIO.OUT, initial=GPIO.HIGH) #a-gsm 2.064
	#GPIO.setup(RESET, GPIO.OUT, initial=GPIO.HIGH) #a-gsm 2.064
        GPIO.setup(POWER, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(RESET, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setwarnings(True)
    
def hwControlRelease():
    GPIO.cleanup()#free GPIO
