from microbit import *
import music

while True:
    display.scroll(display.read_light_level())
    sleep(1000)   
    if display.read_light_level() >= 80:
        #H = High- nivel de iluminación alto
        display.show("H")
        music.play(music.ENTERTAINER)
        display.show(Image.CHESSBOARD)
    else:
        display.clear()
        #L = Low- nivel de iluminación bajo
        display.show("L")
        music.play(music.NYAN)
        display.show(Image.DIAMOND_SMALL)

