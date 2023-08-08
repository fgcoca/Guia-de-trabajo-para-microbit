from microbit import *

#Permite usar los pines de pantalla como entradas externas
display.off() 

#Creamos la lista de pines reasignando el 5 a pin0
pines_salida =[pin1,pin2,pin3,pin4,pin0,pin6,pin7,pin8,pin9,pin10]

while True:
    for pin in pines_salida:
        pin.write_digital(1)
        sleep(150)
        pin.write_digital(0)
        sleep(5)
