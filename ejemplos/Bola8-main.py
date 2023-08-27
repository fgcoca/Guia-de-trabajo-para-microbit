# Magic 8 ball by Nicholas Tollervey. February 2016.
# Bola mágica 8 por Nicholas Tollervey. Febrero 2016.
# Ask a question then shake.
# Haz una pregunta y agita la micro:bit
# This program has been placed into the public domain.
# Este programa es de dominio público.

from microbit import *
import random

respuestas = [
    "Es cierto",
    "Es decididamente así",
    "Sin duda alguna",
    "Sí, definitivamente.",
    "Puedes confiar en ello",
    "Como yo lo veo, sí",
    "Lo más probable",
    "Buenas perspectivas",
    "Si",
    "Los indicios apuntan a que sí",
    "Respuesta dudosa inténtalo de nuevo",
    "Vuelve a preguntar más tarde",
    "Mejor no te lo digo ahora",
    "No se puede predecir ahora",
    "Concéntrate y vuelve a preguntar",
    "No cuentes con ello",
    "Mi respuesta es no",
    "Mis fuentes dicen que no",
    "Perspectivas no tan buenas",
    "Muy dudoso",
]

while True:
    display.show('8')
    if accelerometer.was_gesture('shake'):
        display.clear()
        sleep(1000)
        display.scroll(random.choice(respuestas))
    sleep(10)
