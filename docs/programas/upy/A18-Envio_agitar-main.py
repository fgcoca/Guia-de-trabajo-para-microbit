from microbit import *
import radio
radio.on()
radio.config(channel=50, group=90)

while True:
    if accelerometer.is_gesture('shake'):
        radio.send("Agitar")
    recibido = radio.receive()
    if recibido is not None:
        display.show(recibido)
        sleep(50)
    display.clear()





    
