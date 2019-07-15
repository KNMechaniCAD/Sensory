#!/usr/bin/python3
#Kod do wczytywania do db
#wartości skrętu kierownicy

#Importy
import serial
import io
import mysql.connector as mariadb
import time


#Create connection
mariadb_connection = mariadb.connect(user='root', password='raspberry', database='drive')
cursor = mariadb_connection.cursor()
try:
    ser = serial.Serial('/dev/ttyACM1', timeout=1)
    while True:
        print("Reading angle step value")
        val = ser.readline().strip().decode("utf-8")
        print("Angle value: %s" % val)
        time.sleep(0.2)
        date = time.strftime('%Y-%m-%d %H-%M-%S')
        print("Date: %s" % date)
        cursor.execute("INSERT INTO angle (angle, date) VALUES (%s, %s)", (val, date))
        mariadb_connection.commit()
finally:
    ser.close()
    
