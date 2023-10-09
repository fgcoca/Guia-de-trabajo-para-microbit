from microbit import *
from DHT11_RW import *
uart.init(115200, 8, None, 1)

if name == "main":
    sensor = DHT11(pin0)
    while True:
        try:
            temperatura, humedad = sensor.read()
            uart_write("Temperatura:" + str(temperatura) + " C")
            uart_write("Humedad:" + str(humedad) + "%")
        except Exception as e:
            uart_write("Error: " + str(e))
        time.sleep(10)
