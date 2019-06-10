from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_rotation(180)

r = (255, 0, 0)
o = (255, 127, 0)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 255)
i = (75, 0, 130)
v = (159, 0, 255)
e = (0, 0, 0)
w = (255, 255, 255)
c = (10, 10, 10)


 
image = [
g,g,g,e,e,r,r,r,
g,g,g,e,e,r,r,r,
g,g,g,e,e,r,r,r,
g,g,g,e,e,r,r,r,
g,g,g,e,e,r,r,r,
g,g,g,e,e,r,r,r,
g,g,g,e,e,r,r,r,
g,g,g,e,e,r,r,r
]

while True:
    sense.set_pixels(image)
    time.sleep(1)	    
    sense.show_message("KN MechaniCAD",text_colour=[255,0,0])
    sense.set_pixels(image)
    time.sleep(1)
