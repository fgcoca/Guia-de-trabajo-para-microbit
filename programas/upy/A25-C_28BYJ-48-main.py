from microbit import *
display.off() #Necesario porque Pin3 lo usa la pantalla
Pin = [pin0, pin1, pin2, pin3]
while True:
    for i in Pin:
        for j in Pin:
            if i == j:
                j.write_digital(1)
            else:
                j.write_digital(0)
        #Con 2ms de retardo se aprecia el giro del motor pero apenas
        #se ve el parpadeo de los LEDs.
        #Para apreciar este parpadeo mejor podemos aumentar el retardo
        #a 50ms. En este caso 1ms de retardo puede provocar perdida de 
        #pasos impidiendo que el motor gire.
        sleep(2)
