from microbit import *
"""
pin0.set_touch_mode(pin0.CAPACITIVE)
pin1.set_touch_mode(pin0.CAPACITIVE)
pin2.set_touch_mode(pin0.CAPACITIVE)
"""
while True:
    if (pin0.is_touched() or pin1.is_touched() or pin2.is_touched()):
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
