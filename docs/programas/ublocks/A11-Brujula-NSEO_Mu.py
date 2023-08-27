from microbit import *

compass.calibrate()
while True:
    angulo = compass.heading()
    if angulo < 45:
        display.show("N")
    elif angulo < 135:
        display.show("E")
    elif angulo < 225:
        display.show("S")
    elif angulo < 315:
        display.show("O")
    else:
        display.show("N")
