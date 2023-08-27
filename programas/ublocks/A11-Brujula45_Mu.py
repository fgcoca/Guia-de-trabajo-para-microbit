from microbit import *

compass.calibrate()
while True:
    angulo = compass.heading()
    if angulo > 22.5 and angulo <= 67.5:
        display.show(Image.ARROW_NE)
    elif angulo > 67.5 and angulo <= 112.5:
        display.show(Image.ARROW_E)
    elif angulo > 112.5 and angulo <= 157.5:
        display.show(Image.ARROW_SE)
    elif angulo > 157.5 and angulo <= 202.5:
        display.show(Image.ARROW_S)
    elif angulo > 202.5 and angulo <= 247.5:
        display.show(Image.ARROW_SW)
    elif angulo > 247.5 and angulo <= 292.5:
        display.show(Image.ARROW_W)
    elif angulo > 292.5 and angulo <= 337.5:
        display.show(Image.ARROW_NW)
    elif angulo > 337.5 and angulo <= 22.5:
        display.show(Image.ARROW_N)
