from microbit import *
import radio
radio.on()

#Set to any channel between 0 and 83
radio.config(channel=7)
rec = "0"
while True:
    
    new_rec = radio.receive()
    if new_rec != None:
        rec = new_rec
        
    pin0.write_digital(1)
    
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    coordinates = str(x) + "," + str(y) 
    radio.send(coordinates)
