from microbit import *

while True:
    nivel_luz = display.read_light_level()
    uart.write(str(nivel_luz) + "\r\n")
    sleep(1000)
    