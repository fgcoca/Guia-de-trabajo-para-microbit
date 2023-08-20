from microbit import *

cuenta=0
# Code in a 'while True:' loop repeats forever
while True:
    uart.write('Contador: '+str(cuenta)+"\r\n")
    sleep(1000)
    cuenta=cuenta+1
