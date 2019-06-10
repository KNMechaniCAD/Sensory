############################################################################################################################################
#bgsmgnss_GNSS_Lib.py v1.01/24 March 2017 - b-gsmgnss 2.105 GNSS [GPS+GLONASS] basic functions library
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
from agsm_Serial_Lib import *
from string import replace, len

#lat,lon,hdop,alt,fix,cog,spkm,nsat,date,time
GNSSmessage = ["","","","","","","","","","",""]

def enableGNSS():
        sendATcommand("AT+QGNSSC=1",["OK","ERR"],2)
        #print(getResponse())
        sendATcommand("AT+QGNSSEPO=1",["OK","ERR"],2)
        #print(getResponse())

def disableGNSS():
        sendATcommand("AT+QGNSSC=0",["OK","ERR"],2)
        #print(getResponse())

def getGNSScoordinates():
        global GNSSmessage
        res=0
        res=sendATcommand("AT+QGNSSRD=\"NMEA/GGA\"",["OK","ERR"],2)
        if(res != 0):
                print ("no GPS data available")
                return 1
        buffd = getResponse()
        #print (buffd)
        #+QGNSSRD: $GNGGA,034035.000,3150.8617,N,11711.9038,E,1,4,1.50,40.9,M,0.0,M,,*44
        if(len(buffd)<106):
                print ("no GPS data available")
                return 1
        else:#process data
                processed = buffd.split(",")
                #lat,lon,hdop,alt,fix,cog,spkm,nsat,date,time
                #GNSSmessage = ["","","","","","","","","","",""]
                GNSSmessage[7] = str(processed[7])#nsat
                GNSSmessage[2] = str(processed[8])#hdop
                GNSSmessage[3] = str(processed[9])#alt

        res=sendATcommand("AT+QGNSSRD=\"NMEA/RMC\"",["OK","ERR"],2)
        if(res != 0):
                print ("no GPS data available")
                return 1
        #buffd = getResponse()
        #+QGNSSRD: $GNRMC,034035.000,A,3150.8617,N,11711.9038,E,3.02,183.45,240516,,,A*75print (buffd)
        if(len(buffd)<104):
                print ("no GPS data available")
                return 1
        else:#process data
                processed = buffd.split(",")
                #lat,lon,hdop,alt,fix,cog,spkm,nsat,date,time
                GNSSmessage[8] = str(processed[9])#date
                tstr = str(processed[1])#time
                #tstr[6]=chr(0x00) #remove miliseconds
                #GNSSmessage[9] = tstr#time
                tstr = tstr.split(".") #remove miliseconds
                GNSSmessage[9] = tstr[0]#time
                GNSSmessage[0] = str(processed[3])+str(processed[4])#latitude, latitude N/S
                GNSSmessage[1] = str(processed[5])+str(processed[6])#longitude, longitude E/W

                #GNSSmessage[6] = str(processed[7]*1.852)#spkn
                GNSSmessage[6] = str(int(long(processed[7])*1.852))#spkm from spkn
                GNSSmessage[5] = str(processed[8])#cog
                
        #GNSSmessage[4] = "2"#2D/3D fix ..to be fixed
        res=sendATcommand("AT+QGNSSRD=\"NMEA/GSA\"",["OK","ERR"],2)
        if(res != 0):
                print ("no GPS data available")
                return 1
        buffd = getResponse()
        #+QGNSSRD: $GLGSA,A,3,82,70,,,,,,,,,,,1.75,1.50,0.91*1C
        processed = buffd.split(",")
        if(int(processed[2]) < 2):#no fix
                print ("no GPS data available")
                return 1
        GNSSmessage[4] = str(processed[2]) #fix ==> 2D/3D

        return 0

def getGNSSmessage():
    return GNSSmessage
