from microbit import *
# Ver la entrada servomotor de la sección componentes avanzados
# en el apartado Conceptos tecnicos:
# https://fgcoca.github.io/Guia-de-trabajo-para-microbit/conceptos/avanzados/#el-servomotor
while True:
    pin0.set_analog_period(20)
    for i in range(26,128,1):
        pin0.write_analog(i)
        sleep(10)
    for i in range(128,26,-1):
        pin0.write_analog(i)
        sleep(10)
