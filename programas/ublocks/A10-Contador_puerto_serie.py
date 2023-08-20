from microbit import *

cuenta = 0

while True:
    uart.write("Contador: " + str(cuenta) + "\r\n")
    sleep(1000)
    cuenta = cuenta + 1
