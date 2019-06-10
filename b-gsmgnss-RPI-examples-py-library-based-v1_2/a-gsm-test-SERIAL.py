############################################################################################################################################
#a-gsm-test-SERIAL.py v 1.01/24 March 2017 - a-gsmII/b-gsmgnss 2.105 test SERIAL communication utility
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


usePoweringControl = 1#change it to 0 if you do not want to control powerUP/powerDown the a-gsm board. In this case, please be sure the a-gsm board is powered UP(..see a-gsm_kickstart_v_x-yz.pdf) before run this utility   

#Do not change under following line! Insteed make one copy of the file and play with! 
#Hint: if you make changes of the code, before you run it run clear utility (erase the Python compiled *.pyc files)... 
############################################################################################################################################

import os
import serial
from time import sleep, time
from string import replace

from globalParVar import *
from agsm2_bgsmgnss_105_hw_control import *
from agsm_Serial_Lib import *
from agsm_Basic_Lib import *

# bellow chose value bw [SER] Serial /dev/ttyAMA0 or [USB] /dev/ttyUSB0
# if module USB port maps to other port as /dev/ttyUSB1, just edit the moduleName_Serial_lib.py...
serialCommunicationVia = SERIALCON # here we use the comunication via SERIAL port

if(serialCommunicationVia!=USBCON):
    print "Light example - just testing SERIAL communication (/dev/ttyAMA0)."
else:
    print "Light example - just testing USB communication (/dev/ttyUSB0)."
sleep(1)


print "\r\nHEALTH AND SAFETY WARNING!!!!!!!!!!!!!!!!!!!!HEALTH AND SAFETY WARNING!!!!!!!!!!!!!!!!!!!!"
print "\r\n\r\nHigh power audio module(around 700mW RMS)! You can damage your years! Use it with CARE when HEADSETS are USED."
print "We recomend to use AT+CLVL=20, audio setup command in order to limit the output power."
print "\r\n"
sleep(2)

if not os.getuid() == 0:
    print("please use root privileges! try: \"sudo python yourPythonFileName.py\"")
    exit(0)

# set SERIAL/USB communication section start
setSerialCom(serialCommunicationVia)    # OVERRIDE the default value loaded from globalParVar.py
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
# set MODEM STARTUP SETUP section end        

# MAIN PROGRAM section start        
print("Read IMEI (modem id)")
IMEI=getIMEI()
print(IMEI)
print ""

print("Read IMSI (SIM id)")
IMSI = getIMSI()
print IMSI

print("checking 4 gsm registration")
res = wait4GSMReg(5)
if(res==1):
    print("ready...")

print("Let's check the signal level")
res = getSignalStatus()
print "Signal: "+ str(res)
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

if(serialCommunicationVia!=USBCON):
    print("\r\n\r\nThat's all folks!\r\nMaybe u want to try communication over USB...")
    print("Read config how to in a-gsm-test-USB.py. Configure the hardware and after that run a-gsm-test-USB.py\r\n")
else:
    print("\r\n\r\nThat's all folks!\r\nMaybe u want to try communication over SERIAL...")
    print("Read config how to in a-gsm-test-SERIAL.py. Configure the hardware and after that run a-gsmtest-SERIAL.py\r\n")
