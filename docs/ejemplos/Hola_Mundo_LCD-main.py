# Le indicamos a MicroPython que obtenga todo (el *) lo que 
# necesita para trabajar con micro:bit desde el módulo microbit
from microbit import *
# De idéntica forma le decimos que obtenga todo de la clase
# I2C_LCD1602 para trabajar con una LCD 1602 I2C
from I2C_LCD1602 import *
# Inicializamos el objeto al crear una instancia de 
# la clase a través del self del método dunder __init__
lcd = I2C_LCD1602(0x27)
lcd.on()
lcd.backlight(1) #1=retroiliminación ON, 0=retroiluminacion OFF
lcd.clear()

while True:
    # Escribe Hola Mundo desde la columna 0 en la fila 0.
    lcd.puts("Hola Mundo",0,0) 
    # Escribe LCD I2C1602 desde la columna 3 de la fila 1
    lcd.puts("LCD I2C1602",3,1)
    
