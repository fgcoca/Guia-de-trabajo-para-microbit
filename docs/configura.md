# <FONT COLOR=#8B008B>Configurar nuestra micro:bit</font>
Para poder continuar le tenemos que decir a la micro:bit lo que queremos que haga. Esto es dar a la micro:bit una serie de instrucciones contenidas en programas. Estos programas, en el caso de micro:bit, se pueden escribir de diferentes maneras y nosotros vamos a ver fundamentalmente como hacerlo en los editores online de bloques **MakeCode** y **MicroBlocks** o **Python** de texto.

Debemos disponer de un ordenador, un teléfono o una tableta para escribir el código, conectar la micro:bit a nuestro dispositivo lo que haremos de alguna de estas formas:

* Con ordenador. Es la forma mas usual y sencilla y consiste en utilizar un cable microUSB para realizar la conexión de la micro:bit al ordenador. Esta forma la vamos a describir de manera mas extensa a continuación.
* Teléfono o tableta. En este caso debemos utilizar Bluetooth para conectar ambos dispositivos de manera inalámbrica. Podemos consultar mas detalles en [Transferir desde la aplicación móvil](https://microbit.org/es-es/get-started/first-steps/set-up/), web que además nos va a servir de referencia para el resto de este apartado.

## <FONT COLOR=#007575>**Transferir desde ordenador**</font>
Los programas de usuario se copian en la memoria flash (no volatil) de la micro:bit por lo que a esta operación se le suele conocer como flasheo. La V1 tiene 256 KB de memoria flash y la V2 512 KB

Cuando se está flasheando un programa la micro:bit pausa la ejecución del programa que tenga en memoria y el LED amarillo de la cara posterior estará parpadeando mientras se esté copiando el nuevo programa. Una vez finalizada la copia, el nuevo programa comienza a ejecutarse en la micro:bit.

### <FONT COLOR=#AA0000>Arrastrar y soltar</font>
El proceso es exactamente igual que cuando transferimos un archivo desde el ordenador a un pendrive o memoria USB y funciona en cualquier ordenador. Lo que tenemos que hacer es:

* Descargar el programa como un archivo .hex desde el editor de código al ordenador, habitualmente al directorio de descargas. Finalmente se arrastra y suelta el archivo .hex en la unidad MICROBIT.
* Después de transferir el archivo .hex, la unidad MICROBIT se desconectará y reconectará según la micro:bit se reinicia. El archivo .hex no aparecerá en la unidad MICROBIT dado que la micro:bit no es un dispositivo de almacenamiento flash, aunque el ordenador lo muestra como tal para facilitar la transferencia de archivos .hex.

En el enlace [Transferir desde la aplicación móvil](https://microbit.org/es-es/get-started/first-steps/set-up/) hay disponibles videos que muestran cómo funciona este sistema. Simplemente elegimos nuestro sistema operativo (Windows, Mac, Chromebook o Linux/Raspberry Pi) y vemos el proceso.

En la animación siguiente (descarga de la web citada en el párrafo anterior) vemos el proceso completo en el caso de Linux.

<center>

![Flasheo mediante arrastrar y soltar](../img/configura/arr_soltar.gif)  
*Flasheo mediante arrastrar y soltar*

</center>

### <FONT COLOR=#AA0000>Flasheo directo</font>
Se pueden enviar programas directamente desde los editores de código en línea a la micro:bit sin necesidad de descargar el archivo .hex y seguir el proceso anterior, lo que resulta fácil y rápido.

El flasheo directo solamente funciona en los navegadores Chrome o Edge que soportan webUSB. También es necesario tener actualizado el firmware de la micro:bit, especialmente si es un modelo que tiene mucho tiempo.

**IMPORTANTE**: EL flasheo directo es rápido y fácil, y excelente para la depuración, pero no SE guarda una copia deL programa en el ordenador. Si es importante mantener una copia del código es preferible utilizar el método de arrastrar y soltar, o en su defecto tener siempre la precaución de descargar el archivo .hex cuando se ha completado exitósamente el proyecto aunque durante el proceso se relicen pruebas del funcionamiento o depuración del código mediante este método.

En la web de referencia tenemos disponibles videos demostrativos de como se realiza el proceso.

## <FONT COLOR=#007575>**Algunos problemas con WebUSB**</font>
La información de referencia de lo que se dice aquí está en [WebUSB Troubleshooting](https://support.microbit.org/support/solutions/articles/19000105428-webusb-troubleshooting).

Antes de nada debemos tener en cuenta todo lo indicado referente al sistema operativo, los navegadores compatibles y la versión de firmware requerida.

La micro:bit nos debe aparecer en el navegador como **BBC micro:bit CMSIS-DAP** aunque es posible que la primera vez nos aparezca como *LPC1768*.

Si nos estamos cambiando entre editores, por ejemplo MakeCode y Python, seguramente la actualización de programas mediante webUSB requiere mas tiempo del habitual ya que la micro:bit contiene un programa creado con un editor diferente.

Si tenemos problemas cuando tenemos conectada alimentación externa, procedemos a desconectar esta alimentación y el cable microUSB garantizando asi el total apagado de la placa. Conectamos solamente el cable microUSB tanto a la micro:bit como al ordenador e intentamos de nuevo el flasheo. Es indiferente para esto conectar la bateria tras conectar el cable microUSB o hacerlo en otro momento.

Si estamos en un sistema Linux y se ha instalado Chromium desde snap store, que es la tienda oficial de software de Ubuntu, no podremos acceder a dispositivos webUSB. En distribuciones como Ubuntu suele solucionar el problema declarar una regla [udev](https://es.wikipedia.org/wiki/Udev). A continuación se indica como hacerlo:

* Cerramos el navegador Chrome o Chormium
* Creamos un fichero *50-microbit.rules* en:

~~~
/etc/udev/rules.d/50-microbit.rules
~~~

* El contenido del fichero será:

*SUBSYSTEM=="usb", ATTR{idVendor}=="0d28", MODE="0664", GROUP="plugdev"*

* Añadimos nuestro nombre de usuario al grupo plugdev mediante:

~~~
sudo usermod -a -G plugdev <nombre-usuario>
~~~

* Restablecemos las reglas udev haciendo:

~~~
sudo udevadm control --reload-rules
~~~

* Cerramos sesión.
* Tras iniciar sesión de nuevo abrimos Chrome y lo volvemos a intentar.

## <FONT COLOR=#007575>**Sistema de prueba**</font>
Mediante el hilo indicado en la webgrafia y utilizando la información obtenida de [WebUSB Troubleshooting](https://support.microbit.org/support/solutions/articles/19000105428-webusb-troubleshooting) ha quedado resuelto el tema de utilizar [webUSB con Chromium](directo.md) y se propone un método de prueba de errores que a mi entender nos puede resultar bastante útil en un momento determinado.

Cuando estamos teniendo problemas para grabar firmware mediante la técnica de arrastrar y soltar (drag & drop) y/o flasheando desde la web del editor, nos resultará útil disponer de una colección de archivos que permitan ir realizando pruebas al tiempo que llevamos la cuenta de las pruebas realizadas.

Es **Martin Williams** de **Micro:bit Educational Foundation** quien propone el sistema y el procedimiento a seguir.

* Siempre que tengamos un error tenemos que desconectar y volver a conectar el USB antes de probar de nuevo con el mismo archivo.
* Crear un script de Python en el que podamos ir cambiando el número de intento cuando el programa se flashea o graba correctamente.

El script de Python propuesto lo he modificado y queda así:

~~~python
# Las importaciones al principio
"""En Python, se utiliza la palabra clave import 
para hacer que el código de un módulo esté 
disponible en otro."""
from microbit import *

display.show(Image.HEART)
sleep(1000)

# El código en'while True:' se repite indefinidamente
while True:
    display.show(0) #Contamos cambiando el valor aquí
    sleep(1000)
~~~

En el fichero [10_archivos_hex_python.zip](/docs/programas/upy/coleccion_errores/10_archivos_hex_python.zip) tenemos los 10 archivos hexadecimal generados y probados. El primero de los cuales (python0-main.py) también lo tenemos en formato texto.

<b><font color=#FF0000>En los enlaces a ficheros, en lugar de hacer clic para abrir el enlace, debemos hacer clic en el botón derecho y escoger 'Guardar enlace como'</font></b>
