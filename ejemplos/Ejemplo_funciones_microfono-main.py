'''Prueba básica del micrófono.  
Boton A: actualizar pantalla cuando se escucha un sonido alto o bajo. 
Botón B: actualizar la pantalla cuando se escucho un sonido alto o bajo. 
Al agitarla: se muestran los últimos sonidos escuchados, para intentar esta prueba 
se hace un sonido fuerte y uno silencioso antes de agitar.'''

from microbit import *

display.clear()
sound = microphone.current_event()

while True:
    if button_a.is_pressed():
        if microphone.current_event() == SoundEvent.LOUD:
            display.show(Image.SQUARE)
            uart.write('Es Fuerte\n')
        elif microphone.current_event() == SoundEvent.QUIET:
            display.show(Image.SQUARE_SMALL)
            uart.write('Es Silencio\n')
        sleep(500)
    display.clear()
    if button_b.is_pressed():
        if microphone.was_event(SoundEvent.LOUD):
            display.show(Image.SQUARE)
            uart.write('Fue Fuerte\n')
        elif microphone.was_event(SoundEvent.QUIET):
            display.show(Image.SQUARE_SMALL)
            uart.write('Fue silencioso\n')
        else:
            display.clear()
        sleep(500)
    display.clear()
    if accelerometer.was_gesture('shake'):
        sounds = microphone.get_events()
        soundLevel = microphone.sound_level()
        print(soundLevel)
        for sound in sounds:
            if sound == SoundEvent.LOUD:
                display.show(Image.SQUARE)
            elif sound == SoundEvent.QUIET:
                display.show(Image.SQUARE_SMALL)
            else:
                display.clear()
            print(sound)
            sleep(500)