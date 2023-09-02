from microbit import *
import math  # para los cálculos

while True:
    Temp_int = temperature()
    display.scroll(Temp_int)
    sleep(1000)
    lectura_ADC = pin0.read_analog()
    # Pasa la lectura analogica a voltios
    V = lectura_ADC * 3.3 / 1023.0
    # Por teoria divisor de tension
    Rt = 10 / ((3.3 / V) - 1)
    # Calculo de la temperatura
    Temp_term = 1 / (1 / 25 + math.log(Rt / 10) / 3997)
    Temp_term_int = round(Temp_term)
    display.scroll(round(Temp_term_int))
    sleep(2000)
