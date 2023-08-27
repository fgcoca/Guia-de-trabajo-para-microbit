from microbit import *
import neopixel

# Establecemos el número de LEDs
neop = neopixel.NeoPixel(pin0, 8)
# Función para convertir color HSL en color RGB
# devuelve el valor RGB correspondiente al ángulo del matiz actual.

def HSL_RGB(grados):
    grados=grados/360*255
    if grados < 85:
        red = 255 - grados * 3
        green = grados * 3
        blue = 0
    elif grados < 170:
        grados = grados - 85
        red = 0
        green = 255 - grados * 3
        blue = grados * 3
    else:
        grados = grados - 170
        red = grados * 3
        green = 0
        blue = 255 - grados * 3
    return int(red),int(green),int(blue)

while True:
    for i in range(0, 8):
        # La lectura analogica se convierte al angulo del matiz actual.
        # La diferencia de tono entre cada dos led es de 45
        valor=pin1.read_analog()/1023*360+i*45
        if valor > 360 :
            valor = valor-360
        # Los colores serán los del arcoiris
        red,green,blue=HSL_RGB(valor)
        neop[i] = (red,green,blue)
    neop.show()