from microbit import *

import radio

#left wheel connected to pin0 + pin15
#right wheel connected to pin1 + pin14

radio.on()
radio.config(channel=7)

x = 0
y = 0

#get "normal" field strength
norm = compass.get_field_strength()

#Adjust y if out of bounds
def adjust_val(val):
    if val < -1023:
        val = -1023
    elif val > 1023:
        val = 1023
        
    return val
    
def forward_motion(x,y):
    
    # positive x -> turn to the right
    if x > 0:
        val = x - y
        if val > 1023:
            val = 1023
        pin0.write_analog(val)
        try:
            pin1.write_analog(-y)
        except:
            display.scroll("Forward")

    # negative x -> turn to the left
    if x < 0:
        val = 0 - y - x
        if val > 1023:
            val = 1023
        try:
            pin0.write_analog(-y)
        except:
            display.scroll("backwards")
        pin1.write_analog(val)
        
def backward_motion(x,y):
    # positive x -> turn to the right
    if x > 0:
        val = x - y
        if val > 1023:
            val = 1023
        pin15.write_analog(val)
        try:
            pin14.write_analog(-y)
        except:
            display.scroll(y)

    # negative x -> turn to the left
    if x < 0:
        val = 0 - y - x
        if val > 1023:
            val = 1023
        pin14.write_analog(val) 
        try:
            pin15.write_analog(-y)
        except:
            display.scroll(y)

while True:
    rec = radio.receive()
    
    #variations of 10000 nT are normal
    field_strength = compass.get_field_strength()
    if abs(field_strength-norm) > 10000:
        radio.send("1")
        display.show(Image.NO)
    else:
        radio.send("0")
        display.clear()

    # Has anything been received?
    if rec != None:
        coordinates = rec.split(',')
        x = int(coordinates[0])
        y = int(coordinates[1])
           
    # Adjust y if out of bounds
    y = adjust_val(y)
    
    if y <= 0:
        forward_motion(x,y)
    else:
        backward_motion(x,-y)
  
