from microbit import *
# Poner valor al primero que entra
LSBFIRST=1
MSBFIRST=2

# Definir pines conectados al 74HC595
pinDatos=pin0 # Entrada datos serie - 74HC595(Pin14)
pinDesplaza=pin1 # Desplazamiento - 74HC595(Pin12)
pinRegistro=pin2 # Registro (reloj) - 74HC595(Pin11)

# Funcion para escribir datos en serie en el 74HC595
def desplazar(valor,dPin,cPin,sentido_desp):
    #En el bucle for, el valor de la variable se desplaza a la 
    #izquierda i-bit, la variable se escribe en el 74HC595 y
    #se encienden los LEDs uno a uno a través de la salida paralelo
    for i in range (8):
        cPin.write_digital(0)
        if sentido_desp==MSBFIRST:
            indicador=valor<<i & 0x80 # Cambia 1s a 0s
            if indicador==0x80:
                dPin.write_digital(1)
            else:
                dPin.write_digital(0)
        else:
            indicador=valor>>i & 0x01
            if indicador==0x01:
                dPin.write_digital(1)
            else:
                dPin.write_digital(0)
    cPin.write_digital(1)

while True:
    for i in range(8):
        valor=0x01<<i
        pinDesplaza.write_digital(0)
        desplazar(valor,pinDatos,pinRegistro,LSBFIRST)
        pinDesplaza.write_digital(1)
        sleep(200)
