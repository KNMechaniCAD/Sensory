from sense_hat import SenseHat
from os import system
import time

sense = SenseHat()
sense.clear()

o = sense.get_orientation()

#First measurement
baseP = o["pitch"]
baseR = o["roll"]
baseY = o["yaw"]

while True:
    o = sense.get_orientation()
    readP = o["pitch"]
    readR = o["roll"]
    readY = o["yaw"]
    pitch = readP - baseP
    roll = readR - baseR
    yaw = readY - baseY
    system('clear')
    print("pitch {0} roll {1} yaw {2}".format(round(pitch,2), round(roll,2), round(yaw,2)))
    time.sleep(0.1)
