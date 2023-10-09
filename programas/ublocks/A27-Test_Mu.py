from microbit import *
from I2C_LCD1602 import *  # Agregar desde Archivos

# Habilita pines GPIO
display.off()
teclado = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"],
]
Pines_filas = [pin9, pin6, pin10, pin4]
Pines_col = [pin3, pin2, pin1, pin0]
lcd = I2C_LCD1602(0x27)
lcd.clear()
# Se ponen todos los pines a 0 -->
for i in range(4):
    Pines_filas[i].write_digital(0)
for i in range(4):
    Pines_col[i].write_digital(0)  # <--
while True:
    for i in range(4):
        Pines_filas[i].write_digital(1)
    for j in range(4):
        if Pines_col[j].read_digital() == 1:
            lcd.puts(teclado[i][j], 0, 0)
    Pines_filas[i].write_digital(0)
