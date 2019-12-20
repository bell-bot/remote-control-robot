# Add your Python code here. E.g.
from microbit import *
import radio
radio.on()

while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    coordinates = str(x) + "," + str(y) 
    radio.send(coordinates)
