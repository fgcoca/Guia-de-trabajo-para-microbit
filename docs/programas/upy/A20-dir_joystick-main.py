from microbit import *

while True:
    x = pin2.read_analog()
    y = pin1.read_analog()
    z = pin0.read_digital()
    if z == 0:
        display.clear()
        display.show("0")
    elif x<400 and y<700 and y>400:
        display.show(Image.ARROW_N)
    elif x>700 and y<700 and y>400:
        display.show(Image.ARROW_S)
    elif y>700 and x<700 and x>400:
        display.show(Image.ARROW_W)
    elif y<400 and x<700 and x>400:
        display.show(Image.ARROW_E)
    elif x<400 and y>700:
        display.show(Image.ARROW_NW)
    elif x<400 and y<400:
        display.show(Image.ARROW_NE)
    elif x>700 and y>700:
        display.show(Image.ARROW_SW)
    elif x>700 and y<400:
        display.show(Image.ARROW_SE)
    else:
        display.clear()
        display.show("1")
    sleep(250) # Evita parpadeo