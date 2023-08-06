from microbit import *

while True:
    #Estado_boton = pin0.read_digital()
    #if Estado_boton == 0:
    if pin0.read_digital() == 0:
        pin1.write_digital(1)
    else:
        pin1.write_digital(0)
    
