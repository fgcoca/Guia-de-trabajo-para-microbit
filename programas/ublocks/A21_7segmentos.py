from microbit import *

# Definir listas con definición de caracteres (ver teoria)
num_decimal = [0xC0, 0xF9, 0xA4, 0xB0, 0x99, 0x92, 0x82, 0xF8, 0x80, 0x90]
num_hexadecimal = [
    0xC0,
    0xF9,
    0xA4,
    0xB0,
    0x99,
    0x92,
    0x82,
    0xF8,
    0x80,
    0x90,
    0x88,
    0x83,
    0xC6,
    0xA1,
    0x86,
    0x8E,
]

# Poner valor al primero que entra
LSBFIRST = 1
MSBFIRST = 2

# Definir pines conectados al 74HC595
pinDatos = pin0  # Entrada datos serie - 74HC595(Pin14)
pinDesplaza = pin1  # Desplazamiento - 74HC595(Pin12)
pinRegistro = pin2  # Registro (reloj) - 74HC595(Pin11)


def desplazar(value, dPin, cPin, sentido_desp):
    for i in range(8):
        cPin.write_digital(0)
        if sentido_desp == MSBFIRST:
            indicador = value << i & 0x80  # Cambia 1s a 0s
            if indicador == 0x80:
                dPin.write_digital(1)
            else:
                dPin.write_digital(0)
        else:
            flag = value >> i & 0x01
            if flag == 0x01:
                dPin.write_digital(1)
            else:
                dPin.write_digital(0)
        cPin.write_digital(1)


while True:
    if button_a.was_pressed():
        for numero in num_decimal:
            pinDesplaza.write_digital(0)
            desplazar(numero, pinDatos, pinRegistro, MSBFIRST)
            pinDesplaza.write_digital(1)
            sleep(300)
    if button_b.was_pressed():
        for numero in num_hexadecimal:
            pinDesplaza.write_digital(0)
            desplazar(numero, pinDatos, pinRegistro, MSBFIRST)
            pinDesplaza.write_digital(1)
            sleep(300)
