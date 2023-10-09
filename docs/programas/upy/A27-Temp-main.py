from microbit import *
from I2C_LCD1602 import * # Agregar desde Archivos
display.off() # Habilita pines GPIO
teclado=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Pines_filas = [pin9, pin6, pin10, pin4]
Pines_col = [pin3, pin2, pin1, pin0]
lcd = I2C_LCD1602(0x27)
lcd.clear()
numero=0
# Se ponen todos los pines a 0 -->
for i in range(4):
       Pines_filas[i].write_digital(0)
for i in range(4):
       Pines_col[i].write_digital(0)  # <--
while True:
    for i in range(4):
       Pines_filas[i].write_digital(1)
       for j in range(3):
           if Pines_col[j].read_digital()==1:
               sleep(100)
               if Pines_col[j].read_digital()==1:
                   if i==3 and j==0: #Al pulsar boton "*"
                       numero=0
                       lcd.clear()
                   elif i==3 and j==1:   #Al pulsar boton "0"
                        numero=numero*10
                   elif i==3 and j==2:   #Al pulsar boton "#"
                       while True:
                           lcd.clear()
                           lcd.puts(str(numero), 0, 0)
                           numero-=1
                           sleep(1000) # Velocidad decontar
                           if pin3.read_digital()==1 or numero==0:
                               numero=0
                               lcd.clear()
                               break
                   else:  #Al pulsar boton numerico
                       numero=numero*10+teclado[i][j]
                   lcd.puts(str(numero), 0, 0)
       Pines_filas[i].write_digital(0)