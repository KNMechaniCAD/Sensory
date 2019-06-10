from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

while True:
  temp = sense.get_temperature()
  print(temp)
