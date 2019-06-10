############################################################################################################################################
#bgsmgnss-GNSS-simple.py v1.01/24 March 2017 - b-gsmgnss 2.105  GNSS [GPS+GLONASS] utility / demo
#COPYRIGHT (c) 2017 Dragos Iosub / R&D Software Solutions srl
#
#You are legaly entitled to use this SOFTWARE ONLY IN CONJUNCTION WITH b-gsmgnss DEVICES USAGE. Modifications, derivates and redistribution 
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

usePoweringControl = 1#change it to 0 if you do not want to control powerUP/powerDown the b-gsmgnss board. In this case, please be sure the b-gsmgnss board is powered UP(..see b-gsmgnss_kickstart_v_x-yz.pdf) before run this utility   

#Do not change under following line! Insteed make one copy of the file and play with! 
#Hint: if you make changes of the code, before you run it run clear utility (erase the Python compiled *.pyc files)... 
############################################################################################################################################

import os
import serial
from time import sleep, time

from globalParVar import *
from agsm2_bgsmgnss_105_hw_control.py import *
from agsm_Serial_Lib import *
from agsm_Basic_Lib import *
from bgsmgnss_GNSS_Lib import *

print "Light example - just aquire and print the GNSS [GPS+GLONASS] positions"
sleep(1)

if not os.getuid() == 0:
    print("please use root privileges! try: \"sudo python yourPythonFileName.py\"")
    exit(0)

# set HARDWARE CONTROL setup & POWER ON section start        
if usePoweringControl==1:
    hwControlSetup()                    # setup the RPi I/O ports

sleep(2)#some delay...

if usePoweringControl==1:
    poweron()

sleep(1)
# set HARDWARE CONTROL setup & POWER ON section end        

# set SERIAL/USB communication section start
# bellow chose value bw [SER] Serial /dev/ttyAMA0 or [USB] /dev/ttyUSB3
# if module USB port maps to other port as /dev/ttyUSBx, just edit the globalParVar.py...
#serialCommunicationVia = SERIALCON      # OVERRIDE here, if needed, the default value loaded from globalParVar.py. here I use via SERIAL communication
#setSerialCom(serialCommunicationVia)    # set the current communication option
startSerialCom()                        # open serial communication bw. RPi and b-gsmgnss shield
# set SERIAL/USB communication section end

# set MODEM STARTUP SETUP section start        
setupMODEM()
sleep(1)

print("enable the GNSS engine")
enableGNSS()                            #here enable the GNSS engine
# set MODEM STARTUP SETUP section end

sleep(3)

# MAIN PROGRAM section start        

print "try to read GNSS position in 1000sec loop or 60 position aquired"
i=0
k = 0
while (i < 1000):
    res = getGNSScoordinates()                    #read SMS @ location 1
    if res==0:
        GNSSmessage = getGNSSmessage()        #retrieve the GNSS position
        #lat,lon,hdop,alt,fix,cog,spkm,nsat,date,time
        print "sample: "+str(k)
        print "latitude: "+GNSSmessage[0]
        print "longitude: "+GNSSmessage[1]
        print "HDOP: "+GNSSmessage[2]
        print "altitude: "+ GNSSmessage[3]
        print "fix: "+GNSSmessage[4]+"D"
        print "COG: "+GNSSmessage[5]
        print "speed(km/h): "+GNSSmessage[6]
        print "no. of satellites: "+GNSSmessage[7]
        print "date: "+GNSSmessage[8]
        print "time: "+GNSSmessage[9]
        print ""
        k = k + 1
        if(k > 120):
            i = 1000              #force exit
    else:
        print ("no GPS data available")
    sleep(1)                    #wait 1

sleep(3)
print("disable the GNSS engine")
disableGNSS()                            #here enable the GNSS engine

# MAIN PROGRAM section end        


# HARDWARE CONTROL release & POWER OFF section start        
if usePoweringControl==1:
    poweroff()                              #shutdown modem

if usePoweringControl==1:
    hwControlRelease()                      # free GPIO
# HARDWARE CONTROL release & POWER OFF section end        

# stop SERIAL COMMUNICATION section start        
stopSerialCom()                             # close modem communication
# stop SERIAL COMMUNICATION section end        

print("\r\n\r\nThat's all folks!\r\n")
