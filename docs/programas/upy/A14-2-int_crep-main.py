from microbit import *

while True:
    nivel_luz = pin0.read_analog()
    # Con luz incidiendo en la LDR se obtienen valores bajos.
    # Con la LDR iluminada el valor estará en torno a 1000.
    # Podemos establecer el valor de la comparación 
    # teniendo esto en cuenta.
    uart.write(str(nivel_luz) + "\r\n")
    if nivel_luz > 500:
        pin1.write_digital(1)
    else:
        pin1.write_digital(0)
    