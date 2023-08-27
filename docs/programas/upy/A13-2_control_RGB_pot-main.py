from microbit import *

display.off() #Necesario para poder leer Pin 3
def mapeo(valor,deBajo,deAlto,aBajo,aAlto):
    return (aAlto-aBajo)*(valor-deBajo) / (deAlto-deBajo) + aBajo 
def RGB(grados):
    if grados < 60:
        R = 0
        G = 0
        B = 0
    elif grados < 130:
        R = 0
        G = 0
        B = 255
    elif grados < 200:
        R = 0
        G = 255
        B = 0
    else:
        R = 255
        G = 0
        B = 0
    return R,G,B

while True:
    valor=mapeo(pin3.read_analog(),0,1023,0,270)
    rojo,verde,azul=RGB(valor)
    print(rojo,verde,azul)
    rojo=mapeo(rojo,0,255,1023,0)
    verde=mapeo(verde,0,255,1023,0)
    azul=mapeo(azul,0,255,1023,0)
    pin2.write_analog(int(rojo))
    pin1.write_analog(int(verde))
    pin0.write_analog(int(azul))
    sleep(50)