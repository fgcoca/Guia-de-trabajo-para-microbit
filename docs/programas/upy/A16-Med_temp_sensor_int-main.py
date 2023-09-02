from microbit import *
from I2C_LCD1602 import *

# Creamos una instancia
lcd = I2C_LCD1602(0x27)
lcd.on()
lcd.backlight(1) #1=retroiliminacion ON, 0=retroiluminacion OFF
lcd.clear()

while True:
    Temperatura = temperature()
    display.scroll(Temperatura)
    lcd.puts("Temperatura: ",0,0) 
    lcd.puts(str(Temperatura),5,1)
    lcd.puts("*C ",8,1)
    sleep(2000)
    
