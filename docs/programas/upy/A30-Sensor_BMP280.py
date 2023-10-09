from microbit import *
import I2C_LCD1602
import BMP280

lcd = I2C_LCD1602(0x27)
lcd.on()
lcd.backlight(1)
lcd.clear()
sensor = BMP280.BMP280()
while True:
    presion = str(sensor.read_pressure)
    temperatura = str(sensor.read_temperature)
    lcd.puts("P = ", 0, 0)
    lcd.puts(presion, 4, 0)
    lcd.puts("Pa", 9, 0)
    lcd.puts("T = ", 0, 1)
    lcd.puts(temperatura, 4, 0)
    lcd.puts("*C", 7, 0)
    sleep(1000)
