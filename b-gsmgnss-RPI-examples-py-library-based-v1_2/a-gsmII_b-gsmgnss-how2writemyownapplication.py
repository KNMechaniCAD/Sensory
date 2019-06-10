############################################################################################################################################
#a-gsmII_b-gsmgnss-how2writemyownapplication.py v1.01/24 March 2017 - a-gsmII/b-gsmgnss 2.105 how to write custom application using a-gsm shield python libraries 
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

import os                                       # mandatory
import serial                                   # mandatory
from time import sleep, time                    # optional, depending on your application - here import certain library
from string import replace                      # optional, depending on your application - here import certain library

from globalParVar import *                      # mandatory (import global vars from...), do not change the order
from agsm2_bgsmgnss_105_hw_control import *     # mandatory, do not change the order
from agsm_Serial_Lib import *                   # optional (if you will call here functions from this library), do not change the order
from agsm_Basic_Lib import *                   # mandatory, do not change the order
#from agsm_SMS_Lib import *                    # optional (if you will call here functions from this library), do not change the order
#from agsm_DTMF_Lib import *                   # optional (if you will call here functions from this library), do not change the order
#from agsm_HTTP_Lib import *                   # optional (if you will call here functions from this library), do not change the order
#from myCustomLibrary import *                  # optional (inside write your own functions ), do not change the order

print "Light example - how to write custom application using a-gsm shield python libraries."
sleep(1)
if not os.getuid() == 0:
    print("please use root privileges! try: \"sudo python yourPythonFileName.py\"")
    exit(0)

# set HARDWARE CONTROL setup & POWER ON section start###########################################################
if usePoweringControl==1:
    hwControlSetup()                            # setup the RPi I/O ports

sleep(2)#some delay...

if usePoweringControl==1:
    poweron()                                   # power UP the a-gsm shield

sleep(1)

# set HARDWARE CONTROL setup & POWER ON section end#############################################################      


# set SERIAL/USB communication section start####################################################################
# bellow chose value bw [SER] Serial /dev/ttyAMA0 or [USB] /dev/ttyUSB0
# if module USB port maps to other port as /dev/ttyUSB1, just edit the moduleName_Serial_lib.py...
serialCommunicationVia = SERIALCON      # OVERRIDE here, if needed, the default value loaded from globalParVar.py. here I use via SERIAL communication
setSerialCom(serialCommunicationVia)    # set the current communication option
startSerialCom()                        # open serial communication bw. RPi and a-gsm shield 
# set SERIAL/USB communication section end######################################################################


# set MODEM STARTUP SETUP section start#########################################################################
setupMODEM()

#yourCustomStartupFunction()                # call here any "startup" functions you like
# set MODEM STARTUP SETUP section end###########################################################################

# MAIN PROGRAM section start####################################################################################        

                                            # your main code here    
# MAIN PROGRAM section end######################################################################################        


# HARDWARE CONTROL release & POWER OFF section start############################################################
if usePoweringControl==1:
    poweroff()                              #shutdown modem
if usePoweringControl==1:
    hwControlRelease()                      # free GPIO
# HARDWARE CONTROL release & POWER OFF section end##############################################################


# stop SERIAL COMMUNICATION section start#######################################################################        
stopSerialCom()                             # close modem communication
# stop SERIAL COMMUNICATION section end#########################################################################


print("\r\n\r\nThat's all folks!\r\n")
