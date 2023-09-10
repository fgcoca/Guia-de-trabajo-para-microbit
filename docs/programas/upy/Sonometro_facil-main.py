from microbit import *

# definicion funcion mapea para cambiar un rango de valores a otro
def mapea(valor, deMin, deMax, aMin, aMax):
    deRango = deMax - deMin
    aRango = aMax - aMin
    valorEsc_de = float(valor - deMin)/float(deRango)
    valorEsc_a = aMin + (valorEsc_de * aRango)
    return valorEsc_a

# Creamos los imagenes para el grafico de barras
grafico5 = Image("99999:"
                 "99999:"
                 "99999:"
                 "99999:"
                 "99999")

grafico4 = Image("00000:"
                 "99999:"
                 "99999:"
                 "99999:"
                 "99999")

grafico3 = Image("00000:"
                 "00000:"
                 "99999:"
                 "99999:"
                 "99999")

grafico2 = Image("00000:"
                 "00000:"
                 "00000:"
                 "99999:"
                 "99999")

grafico1 = Image("00000:"
                 "00000:"
                 "00000:"
                 "00000:"
                 "99999")
               
grafico0 = Image("00000:"
                 "00000:"
                 "00000:"
                 "00000:"
                 "00000")

graficos = [grafico0, grafico1, grafico2, grafico3, grafico4, grafico5]
               
# ignora el primer nivel de sonido leido
nivelSonido = microphone.sound_level()
sleep(200)
# establece un umbral para el nivel de sonido
umbral = microphone.set_threshold(SoundEvent.LOUD, 125)
while True:
    # si el umbral es superado se muestra una carita triste
    if microphone.sound_level() >= 125:
        display.show(Image.SAD)
        sleep(1000)
    else:
        # mapear nivel de sonido de 0-255 a 0-5 para escoger gráfico
        nivelSonido = int(mapea(microphone.sound_level(), 0, 255, 0, 5))
        display.show(graficos[nivelSonido])
