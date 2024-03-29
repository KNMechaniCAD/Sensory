############################################################################################################################################
#a-gsm-send-MMS.py v1.01/24 March 2017 - a-gsmII/b-gsmgnss 2.105 MMS send utility / demo
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


messageSubject      = "test MMS sent from RPI"
message             = "Hi!\r\nThis MMS was sent from the a-gsmII/b-gsmgnss v2.105 shield connected with my RPi board." 
destinationNumber   = "" #usually phone number with International prefix eg. +40 for Romania - in some networks you must use domestic numbers
#the destinationNumber can be also an email address

usePoweringControl = 1  #change it to 0 if you do not want to control powerUP/powerDown the a-gsm board. In this case, please be sure the a-gsm board is powered UP(..see a-gsm_kickstart_v_x-yz.pdf) before run this utility   

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
from agsm_MMS_Lib import *

print "Light example - send an MMS using RPI and a-gsm."
sleep(3)
print "\r\n\r\n***MMS must be supported by SIM plan & check the MMS settings in \"agsm_MMS_Lib.py\"***\r\n"

sleep(5)


if not os.getuid() == 0:
    print("please use root privileges! try: \"sudo python yourPythonFileName.py\"")
    exit(0)
if destinationNumber=="":
    print("No destination number/email address has been set for your MMS!")
    print("Edit the file and set the destinationNumber in line 36\r\n")
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
# set MODEM STARTUP SETUP section end        

# MAIN PROGRAM section start        
print "waiting max 10secs. 4 GPRS registration ..."
wait4GPRSReg(10)                        #check and wait max. 10 sec. for GPRS registration

loadMMSMode()                           # call this "setup" before you performe any MMS related task  

#sanitation tasks
clearMMS()                              # clear any MMS content
delAttachement("*")                     # preliminary task
deactMMSPDP()                           # preliminary task

#set up destination and subject
print "set MMS receipment ...\r\n"
addReceipment(destinationNumber)
sleep(0.2)

print "set MMS subject ...\r\n"
setMMSSubject(messageSubject)
sleep(0.2)

#prepare attachments - You can add multiple files (text, images...)
print "upload the MMS content to the RAM disk ...\r\n"
uplAttachement("msg.txt",message)       # upload & save message attachment to the RAM disk...set proper file extension
sleep(0.2)
print "attach the uploaded file to the MMS ...\r\n"
addAttachement("msg.txt")                # attach to the MMS the previously uploaded msg.txt
sleep(0.2)

# now all are prepared. send the MMS.
print "set MMS subject ...\r\n"
res = sendMMS()
if(res==0):
    print "succeed\r\n"
else:
    print "failed\r\n"

sleep(0.2)

print "clear the previusly uploaded file from the RAM disk ...\r\n\r\n"
delAttachement("msg.txt")
sleep(0.2)

print("You may like implement a sort of file upload from the RPI volumes to the modem RAM disk.\r\n\r\n")

sleep(2)
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
