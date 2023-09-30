from microbit import *

CAMBIAR_estado = False

def write_pin0(CAMBIAR_flag):
    if CAMBIAR_flag:
        pin0.write_digital(1)
    else:
        pin0.write_digital(0)
        
while True:
    if button_a.was_pressed():
        CAMBIAR_estado = not CAMBIAR_estado
        write_pin0(CAMBIAR_estado)
