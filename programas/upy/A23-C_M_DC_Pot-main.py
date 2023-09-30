'''Movemos el cursor del potenciometro lentamente mientras vamos 
viendo en el terminal serie el valor de lectura_pot. Mientras
lo hacemos observamos el funcionamiento del motor.
Debido a la inercia del motor es posible que no empiece a funcionar
en los valores exactos establecidos, dado que el valor PWM generado
no lo hace posible'''
from microbit import *
while True:
    lectura_pot=pin0.read_analog()
    print(lectura_pot) # Ayuda para mover el potenciometro
    if lectura_pot<=400:
        pin2.write_digital(0)
        pin1.write_analog(int((400-lectura_pot)/400*1023))
        pin1.set_analog_period(20)
    elif lectura_pot>=600:
        pin1.write_digital(0)
        pin2.write_analog(int((lectura_pot-600)/400*1023))
        pin2.set_analog_period(20)
    else:
        pin1.write_digital(1)
        pin2.write_digital(1)
