from microbit import *

def mapeo(valor,deBajo,deAlto,aBajo,aAlto):
    return (aAlto-aBajo)*(valor-deBajo) / (deAlto-deBajo) + aBajo 

while True:
    valor=pin0.read_analog()
    pin1.set_analog_period(20)
    # Ver apartado "Control de posición con Python" en el
    # apartado correspondiente
    pin1.write_analog(int((mapeo(valor,0,1023,128,25))))
