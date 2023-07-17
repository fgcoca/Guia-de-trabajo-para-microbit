# Las importaciones van a la cabeza
from microbit import * #Usar todo de la biblioteca microbit
display.clear() #Borra pantalla
display.scroll('Hola Mundo!', delay=50) #Desplaza el texto por pantalla
sleep(1000) #Espera 1s
display.show(Image.HAPPY) #Muestra carita alegre
sleep(1000)
display.clear()
display.set_pixel(0,0,6) #Encendemos pixel al brillo establecido
display.set_pixel(2,2,9)
display.set_pixel(4,0,3)




