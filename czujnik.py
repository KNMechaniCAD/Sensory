import RPi.GPIO as GPIO

#konfiguracja
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

while True:
    print(GPIO.input(23))
