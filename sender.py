from microbit import *
import radio
radio.on()

#Set to any channel between 0 and 100
radio.config(channel=7)

while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    coordinates = str(x) + "," + str(y) 
    radio.send(coordinates)
