############################################################################################################################################
#a-gsm-dial.py v1.01/24 March 2017 - a-gsmII/b-gsmgnss 2.105 dial utility / demo
#COPYRIGHT (c) 2017 Dragos Iosub / R&D Software Solutions srl
#
#You are legaly entitled to use this SOFTWARE ONLY IN CONJUNCTION WITH a-gsmII/b-gsmgnss DEVICES USAGE. Modifications, derivates and redistribution 
#of this software must include unmodified this COPYRIGHT NOTICE. You can redistribute this SOFTWARE and/or modify it under the terms 
#of this COPYRIGHT NOTICE. Any other usage may be permited only after written notice of Dragos Iosub / R&D Software Solutions srl.
#
#This SOFTWARE is distributed is provide "AS IS" in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied 
#warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
#Dragos Iosub, Bucharest 2017.
#http://itbrainpower.net
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
# this utility must be runned as root (just use: sudo python yourPythonFileName.py)


destinationNumber=""#usually phone number with International prefix eg. +40 for Romania - in some networks you must use domestic numbers

import os
import serial
from time import sleep, time
from string import replace

from globalParVar import *
from agsm2_bgsmgnss_105_hw_control import *
from agsm_Serial_Lib import *
from agsm_Basic_Lib import *

print "Light example - dial/redial(for max. "+str(maxDialRetry)+" tries) a destination number, waiting for remote to answer."
print "After the call it is connected, wait for remote to hang up or for max. "+str(maxConTime)+" secs. before local hang up."
sleep(1)
print "\r\nHEALTH AND SAFETY WARNING!!!!!!!!!!!!!!!!!!!!HEALTH AND SAFETY WARNING!!!!!!!!!!!!!!!!!!!!"
print "\r\n\r\nHigh power audio module(around 870mW a-gsmII, 800mW b-gsmgnss)! You can damage your years! Use it with CARE when HEADSETS are USED."
print "We recomend to use AT+CLVL=20, audio setup command in order to limit the output power."
print "\r\n"
sleep(2)

if not os.getuid() == 0:
    print("please use root privileges! try: \"sudo python yourPythonFileName.py\"")
    exit(0)

if destinationNumber=="":
    print("No destination number has been set!")
    print("Edit the file and set the destinationNumber in line 64\r\n")
    exit(0)

# set SERIAL/USB communication section start
# bellow chose value bw [SER] Serial /dev/ttyAMA0 or [USB] /dev/ttyUSB0
# if module USB port maps to other port as /dev/ttyUSB1, just edit the moduleName_Serial_lib.py...
serialCommunicationVia = SERIALCON      # OVERRIDE the default value loaded from globalParVar.py. here I use via SERIAL communication
setSerialCom(serialCommunicationVia)    # set the current communication option
startSerialCom()                        # open serial communication bw. RPi and a-gsm shield
# set SERIAL/USB communication section end

# set HARDWARE CONTROL setup & POWER ON section start        
if usePoweringControl==1:
    hwControlSetup()                    # setup the RPi I/O ports

sleep(2)#some delay...

if usePoweringControl==1:
    poweron()

sleep(1)
# set HARDWARE CONTROL setup & POWER ON section end        

# set MODEM STARTUP SETUP section start        
setupMODEM()
print "init audio channel ..."
setAUDIOchannel()
# set MODEM STARTUP SETUP section end        

# MAIN PROGRAM section start        
print "dialing ..."
run = 1
count = 1
#dial/redial/call connected detection loop
res = dial(destinationNumber)
while(run==1):
    res = getcallStatus()
    if(res==0):     #here the other part answer the call...status active
        #sleep(30)   #you can talk 30 seconds
        #hangup()    #hang up the call 
        print("call connected detected...")
        run=0       #call connected event detected => exit loop
    elif(res<0):    #no calls, you may want to redial??
        if (count>=maxDialRetry):
            print("max redialing... giving up...")
            run=0   #max count...exit loop
        else:
            count+=1
            sleep(1.5)
            print("redialing...")
            dial(destinationNumber)
    sleep(0.2)

startTime = time()
run = 1
res = getcallStatus()
if (res==0):                                        #call connected
    while(run==1):
        res = getcallStatus()
        if(res==0):                                 #call connected
            if(time() - startTime > maxConTime):    #looking for maxConTime sec maximum connection time
                print("max time... hang up...")
                hangup()
                run=0
            sleep(0.5)                              #wait 500 msec
        else:
            print("call is no more active...")
            run=0                                   #exit loop

sleep(1)
# MAIN PROGRAM section end        

# stop SERIAL COMMUNICATION section start        
stopSerialCom()                             # close modem communication
# stop SERIAL COMMUNICATION section end        

# HARDWARE CONTROL release & POWER OFF section start        
if usePoweringControl==1:
    poweroff()                              #shutdown modem

if usePoweringControl==1:
    hwControlRelease()                      # free GPIO
# HARDWARE CONTROL release & POWER OFF section end        

print("\r\n\r\nThat's all folks!\r\n")
