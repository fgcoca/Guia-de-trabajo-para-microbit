from microbit import *
#agregar archivo a proyecto desde menu Project
from I2C_LCD1602 import *
display.off() #habilita pines GPIO
teclas=[["1", "2", "3", "A"], ["4", "5", "6", "B"], ["7", "8", "9", "C"], ["*", "0", "#", "D"]]
Filas = [pin9, pin6, pin10, pin4]
Columnas = [pin3, pin2, pin1, pin0]
lcd = I2C_LCD1602(0x27) #crea objeto lcd
lcd.clear()
#poner todos los pins a 0 -->>
for i in range(4):
    Filas[i].write_digital(0)
for i in range(4):
    Columnas[i].write_digital(0) # <<-- 
while True:
    for i in range(4):
        Filas[i].write_digital(1)
        for j in range(4):
            if Columnas[j].read_digital()==1:
                lcd.puts(teclas[i][j], 0, 0)
        Filas[i].write_digital(0)
