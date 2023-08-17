from microbit import *

while True:
    for i in range(5):
        pin0.write_digital(1)
        sleep(200)
        pin0.write_digital(0)
        sleep(200)
    sleep(2000)