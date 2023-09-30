from microbit import *

while True:
    x = pin2.read_analog()
    y = pin1.read_analog()
    z = pin0.read_digital()
    print("x =",x,"y =",y,"z =",z)
    if z==1:
        display.show(0)
    else:
        display.show(1)
    sleep(1000)
