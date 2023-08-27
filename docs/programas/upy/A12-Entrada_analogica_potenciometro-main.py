from microbit import *

while True:
    lectura_ADC = pin0.read_analog()
    ADC_voltios = lectura_ADC/1024*3.3
    uart.write("Voltaje: " + str(ADC_voltios))
    uart.write("\r\n")
    sleep(1000)
