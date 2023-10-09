from microbit import *
from I2C_LCD1602 import *
from time import sleep_us,ticks_us
# Funcion para el calculo de la distancia
def calcular_distancia():
    distancia=0
    ## Genera el pulso de disparo -->
    pin1.write_digital(1)
    sleep_us(15)
    pin1.write_digital(0)
    ##<--
    while pin0.read_digital() == 0:
        pass #Maneja la condicion sin que el bucle este afectado 
    if pin0.read_digital() == 1:
        ts = ticks_us()
        while pin0.read_digital() == 1:
            pass
        te = ticks_us()
        tc = te - ts
        print(te,ts)
        distancia = (tc*170)*0.0001
    return distancia
lcd = I2C_LCD1602(0x27)
while True:
    distancia=round(calcular_distancia())
    lcd.clear()
    lcd.puts("La distancia es:",0,0)
    lcd.puts(str(distancia),5,1)
    lcd.puts("cm",9,1)
    sleep(2000)
