from microbit import *

while True:
    for i in range(255):
        pin0.write_analog(i)
        sleep(10)
    #bucle decreciente: 
        #se antepone al rango reversed
    for j in reversed(range(255)):
        pin0.write_analog(j)
        sleep(10)