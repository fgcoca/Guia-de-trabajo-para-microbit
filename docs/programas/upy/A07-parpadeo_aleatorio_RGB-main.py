from microbit import *

#Importamos módulo random
import random

while True:
    #Generamos RGB aleatorio
    R=random.randint(0,1023)
    G=random.randint(0,1023)
    B=random.randint(0,1023)

    #Escribe RGB aleatorio en pines
    pin2.write_analog(R)
    pin1.write_analog(G)
    pin0.write_analog(B)
    sleep(1000)

    #Apaga los tres LED
    pin2.write_analog(1023)
    pin1.write_analog(1023)
    pin0.write_analog(1023)
    sleep(1000)
