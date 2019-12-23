# Add your Python code here. E.g.
from microbit import *

import radio

#left wheel connected to pin0 + pin15
#right wheel connected to pin1 + pin16

radio.on()
radio.config(channel=7)

x = 0
y = 0

#Adjust y if out of bounds
def adjust_val(val):
    if val < -1023:
        val = -1023
    elif val > 1023:
        val = 1023
        
    return val
        

while True:
    rec = radio.receive()

    # Has anything been received?
    if rec != None:
        x_and_y = rec.split(',')
        x = int(x_and_y[0])
        y = int(x_and_y[1])
           
    # Adjust y if out of bounds
    y = adjust_val(y)
    
    if y <= 0:
        pin0.write_analog(-y)
        pin1.write_analog(-y)
    else:
        pin15.write_analog(y)
        pin16.write_analog(y)
   
    # positive x -> turn to the right
    """if x > 0:
        val = x - y
        if val > 1023:
            val = 1023
        pin0.write_analog(val)
        try:
            pin1.write_analog(-y)
        except:
            display.scroll(y)

    # negative x -> turn to the left
    if x < 0:
        val = 0 - y - x
        if val > 1023:
            val = 1023
        try:
            pin0.write_analog(-y)
        except:
            display.scroll(y)
        pin1.write_analog(val) 
"""