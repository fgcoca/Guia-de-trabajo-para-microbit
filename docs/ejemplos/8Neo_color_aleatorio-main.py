from microbit import *
import neopixel
"""
    Muestra de manera continuada colores aleatorios en los LEDs
    El ejemplo se realiza para un anillo o tira de 8 LEDs WS2812 conectados a pin0
"""
from random import randint

# Configuramos los Neopixel en pin0 y tira de 8 pixeles
neo = neopixel.NeoPixel(pin0, 8)
num_pixel = 0

while True:
    # Iteramos sobre cada LED de la tira

    if num_pixel < 7:
        for num_pixel in range(0, len(neo)):
            rojo = randint(0, 60)
            verde = randint(0, 60)
            azul = randint(0, 60)
    
            # Asigna al LED actual un valor aleatorio de rojo, verde y azul entre 0 y 60
            neo[num_pixel] = (rojo, verde, azul)
    
            # Muestra los datos actuales en la tira
            neo.show()
            sleep(100)
        else:
            neo.clear()
            sleep(100)
            num_pixel = 0
            
        
        