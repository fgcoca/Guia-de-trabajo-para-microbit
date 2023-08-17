from microbit import *
import music

notas = ['C','D','E','F','G','A','B']
notasS = ['C#','D#','E','F#','G#','A#','B']
while True:
    if button_a.is_pressed():
        music.play(notas)
    if button_b.is_pressed():
        music.play(notasS)






    