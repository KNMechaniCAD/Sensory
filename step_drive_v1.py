#!/usr/bin/python3
#Kod do wczytywania do db
#wartości nastaw prędkości

#Importy
import serial
import io
import mysql.connector as mariadb
import time


#Create connection
mariadb_connection = mariadb.connect(user='root', password='raspberry', database='drive')
cursor = mariadb_connection.cursor()
try:
    ser = serial.Serial('/dev/ttyACM0', timeout=1)
    while True:
        print("Reading step value")
        val = ser.readline().strip().decode("utf-8")
        print("Step value: %s" % val)
        time.sleep(0.2)
        date = time.strftime('%Y-%m-%d %H-%M-%S')
        print("Date: %s" % date)
        cursor.execute("INSERT INTO step (step, date) VALUES (%s, %s)", (val, date))
        mariadb_connection.commit()
finally:
    ser.close()
    
