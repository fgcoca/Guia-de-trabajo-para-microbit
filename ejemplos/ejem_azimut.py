from microbit import *

compass.calibrate()
while True:
    azimut = compass.heading()
    uart.write(str(azimut) + "\r\n")
    sleep(1000)
