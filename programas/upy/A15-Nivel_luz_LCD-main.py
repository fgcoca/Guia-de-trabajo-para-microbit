from microbit import *
from I2C_LCD1602 import *

# Creamos una instancia
lcd = I2C_LCD1602(0x27)
lcd.on()
lcd.backlight(1) #1=retroiliminación ON, 0=retroiluminacion OFF
lcd.clear()

while True:
    # Asigna a variable la lectura recibida por los LEDs de la pantalla
    nivel_luz = display.read_light_level()
    lcd.puts("Nivel de luz: ",0,0) 
    lcd.puts(str(nivel_luz),5,1)
    
