from microbit import *
from I2C_LCD1602 import *
import math #para los cálculos

lcd = I2C_LCD1602(0x27)
lcd.on()
lcd.backlight(1) #1=retroiliminacion ON, 0=retroiluminacion OFF
lcd.clear()

while True:
    Temp_int = temperature()
    display.scroll(Temp_int)
    sleep(1000)
    lectura_ADC = pin0.read_analog()
    # Pasa la lectura analogica a voltios
    V = lectura_ADC*3.3/1023.0
    # Por teoria divisor de tension
    Rt = 10/((3.3/V)-1) #V/(3.3 - V)/10
    # Calculo de la temperatura
    Temp_term = (1/(1/25 + math.log(Rt/10)/3997))
    Temp_term_int = round(Temp_term)
    lcd.puts("T_inter / T_term ",0,0)
    display.scroll(round(Temp_term_int))
    lcd.puts(str(Temp_int),0,1)
    lcd.puts("*C ",3,1)
    lcd.puts(str(Temp_term_int),10,1)
    lcd.puts("*C ",13,1)
    sleep(2000)
    
