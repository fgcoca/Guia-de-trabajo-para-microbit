# <FONT COLOR=#8B008B>Python</font>
De manera muy resumida lo que haremos en esta sección es:

* Introducir los conceptos de programación para programar la micro:bit desde BBC micro:bit MicroPython.
* También introduciremos conceptos de micro:bit Micropython API.

## <FONT COLOR=#007575>**API: El módulo microbit**</font>
Todo lo necesario para interactuar con el hardware de la micro:bit está en el módulo *microbit* y se recomienda su uso escribiendo al principio del programa:

<center>
~~~python
from microbit import *
~~~
</center>

Las funciones disponibles directamente son:

~~~python
sleep(ms) #1
running_time() #2
temperature() #3
scale(valor_a_convertir, from_=(min, max), to=(min, max)) #4
panic(error_code) #5
reset() #6
set_volume(valor) #7 (V2)
'''
1 Esperar el número de milisegundos indicado
2 Devuelve el tiempo en ms desde la última vez que se encendió la micro:bit
3 Devuelve la temperatura en Celcius
4 Convierte un número de una escala de valores a otra
5 La micro:bit entra en modo pánico por falta de memoria y se dibuja una
cara triste en la pantalla. El valor de error_code puede ser cualquier entero.
6 Resetea la micro:bit
7 Estable el volumen de salida con un *valor* entre 0 y 255
'''
~~~

## <FONT COLOR=#007575>API: *Display*</font>
Control de la matriz de 5x5 LEDs que en micro:bit se conoce como pantalla. Los métodos de la clase son:

~~~python
display.get_pixel(x, y) #1
display.set_pixel(x, y, val) #2
display.clear() #3
display.show(image, delay=0, wait=True, loop=False, clear=False) #4
display.scroll(string, delay=400) #5
'''
1 Obtiene el brillo [0 (apagado) a 9 (máx))] del pixel (x,y)
2 Establece el brillo [0 (apagado) a 9 (máx))] del pixel (x,y)
3 Borra (apaga) la pantalla
4 Muestra la imagen
5 Desplaza una cadena por la pantalla a la velocidad en ms del *delay*
'''
~~~

En ambos casos de la API existen otras muchas opciones no incluidas. La funcionalidad de autocompletar nos ayudará para no tener que recordar la sintaxis y conocer las que no aparece aquí. En la animación siguiente vemos un ejemplo de ambos casos.

<center>

![Autocompletar funciones y métodos](../img/programacion/python/func_metodos.gif)  
*Autocompletar funciones y métodos*

</center>

## <FONT COLOR=#007575>**Las listas en Python**</font>
Se trata de un tipo de dato que permite almacenar series de datos de cualquier tipo bajo su estructura. Se suelen asociar a las matrices o arrays de otros lenguajes de programación.

En Python las listas son muy versatiles permitiendo almacenar un conjunto arbitrario de datos. Es decir, podemos guardar en ellas lo que sea.

Una lista se crea con [] y sus elementos se separan por comas. Una gran ventaja es que pueden tener datos de diferentes tipos.

~~~python
lista = [1, "Hola", 3.141592, [1 , 2, 3], Image.HAPPY]
~~~

Las de principales propiedades de las listas:

* Son ordenadas, mantienen el orden en el que han sido definidas
* Pueden ser formadas por tipos arbitrarios de datos
* Pueden ser indexadas con [i]
* Se pueden anidar, es decir, meter una lista dentro de otra
* Son mutables, ya que sus elementos pueden ser modificados
* Son dinámicas, ya que se pueden añadir o eliminar elementos

Evidentemente queda muchas cosas que aprender sobre las listas, pero con estos conocimientos tendremos suficiente para hacer lo que pretendemos, que no es otra cosa que animar imágenes.

## <FONT COLOR=#007575>**Bucles**</font>
Los **Bucles** son un tipo de estructura de control muy útil cuando queremos repetir un bloque de código varias veces. En Python existen dos tipos de bloques, el bucle ***for*** para contar la cantidad de veces que se ejecuta un bloque de código, y el bucle ***while*** que realiza la acción hasta que la condición especificada no sea cierta.

### <FONT COLOR=#AA0000>While</font>
La sintaxis de while es la siguiente:


~~~python
while condicion:
    bloque de codigo
~~~

donde "condicion", que se evalúa en cada iteración, puede ser cualquier expresión realizado con operadores condicionales que devuelva como resultado un valor True o False. Mientra que "bloque de codigo" es el conjunto de instrucciones que se estarán ejecutando mientras la condición sea verdadera (True o '1'). Es lo mismo poner ```while true:``` que poner ```while 1:```.

Para recorrer los bucles se utilizan variables que forman parte de la condición, estableciendose en esta lo que deben cumplir.

Un ejemplo sencillo podría ser el siguiente, controlar el riego de una planta en función del valor de la humedad de la tierra en la que está.

~~~py
from microbit import *

while (humedad() < 45):
    display.scroll(Image.SAD)
    sleep(1000)

display.show(Image.HAPPY)
~~~

que hará que si la humedad baja por debajo de 45 se muestre una carita triste indicando que hay que regar y si es mayor mostrará una carita feliz. Evidentemente hay que resolver el tema de como obtener la humedad, pero esa es una historia que veremos mas adelante.

El bucle ```while``` puede tener de manera opcional un bloque ```else``` cuyas sentencias se ejecutan cuando se han realizado todas las iteraciones del bucle. Un ejemplo lo vemos a continuación:

~~~py
cuenta = 0
while cuenta < 5:
    print("Iteración del bucle")
    cuenta = cuenta + 1
else:
    print("bucle finalizado")
~~~

### <FONT COLOR=#AA0000>for</font>
Son también bucles pero su acción está dirigida a contar el número de veces que ocurre algo o realizar una acción un determinado número de veces. Es especialmente útil para recorrer los datos de una lista, tupla o diccionario.

La sintaxis de este tipo de bucles en Python es:

~~~py
for variable in secuencia:
    declaracion
~~~

Siendo "variable" la variable que se va a recorrer en el bucle de forma que cuando se alcance el valor establecido se sale del bucle.

La variable puede ser una cadena, un rango de valores que se expresa con ```range(n)```, siendo n el número de valores del rango que se inicia en 0 y que pueden ser iterados con una variable. Mas ampliamente, la sintaxis de ```range()``` es ```range(start, stop, step)``` siendo ```start``` y ```stop``` opcionales.

Veamos un primer ejemplo en el que vamos a utilizar un bucle para encender uno a uno por filas los LEDs de la primera y última columna.

~~~py
from microbit import *
for var in range(5): # var puede tomar 5 valores, del 0 al 4
    display.set_pixel(0, var, 9) # Se ilumina el LED de la fila 0 y el valor de var para columna
    sleep(300)
    display.set_pixel(4, var, 9) # Se ilumina el LED de la fila 4 y el valor de var para columna
    sleep(300)
~~~

Los bucles se pueden anidar, es decir se puede crear un bucle dentro de otro del mismo o diferente tipo, de forma que por cada iteración del bucle mas externo se tienen que producir todas las iteraciones del bucle mas interno. Veamos como ejemplo el de encender todos los LEDs de uno en uno, de izquierda a derecha, utilizando el valor de sus coordenadas x,y. El programa sería:

~~~py
from microbit import *

display.clear()
for y in range(0, 5): # Valor de columna
    for x in range(0, 5): # Valor de fila
        display.set_pixel(x, y, 9) # Encender LED x,y
        sleep(100)
~~~

En la animación siguiente vemos el programa en funcionamiento.

<center>

![Uso de bucle for](../img/programacion/python/uso_for.gif)  
*Uso de bucle for*

</center>

El bucle ```for``` puede tener de manera opcional un bloque ```else``` cuyas sentencias se ejecutan cuando se han realizado todas las iteraciones del bucle. Un ejemplo lo vemos a continuación:

~~~py
for var in range(5):
    print(var)
else:
    print("bucle finalizado")
~~~

### <FONT COLOR=#AA0000>Bucle for decontando</font>
Se trata del mismo bucle ```for``` pero ahora la cuenta la realizamos hacia atrás. Hay dos formas sencillas de hacerlo:

* Utilizando la función ```range()```. Si queremos darle un enfoque Pythonic simplemente configuramos los argumentos de la función de manera que se indique el principio, el final y el incremento, que será logicamente negativo.

~~~py
for i in range(20, 0, -2): #imprimere 20, 18, 16, ... 0
~~~

* Utilizando la función ```reversed()```. Es una función incorporada en la que hay que indicar como primer argumento el final de la cuenta, como segundo el principio, teniendo en cuenta que se omite, y como tercero el decremento si es ditintos de 1, pero se especifica en módulo. Se utiliza así:

~~~py
for i in reversed(range(0,21,2)): #imprimere 20, 18, 16, ... 0
~~~

### <FONT COLOR=#AA0000>Sentencias ```break``` y ```continue```</font>
La sentencia ```break``` se utiliza para terminar un bucle de forma inmediata al ser encontrada. En la imagen vemos la sintaxis de la sentencia ```break``` y su funcionamiento.

<center>

![Sintaxis y funcionamiento de break](../img/programacion/python/break.png)  
*Sintaxis y funcionamiento de ```break```*

</center>

La sentencia ```continue``` se utiliza para saltar la iteración actual del bucle y el flujo de control del programa pasa a la siguiente iteración. En la imagen vemos la sintaxis de la sentencia ```continue``` y su funcionamiento.

<center>

![Sintaxis y funcionamiento de continue](../img/programacion/python/continue.png)  
*Sintaxis y funcionamiento de ```continue```*

</center>

En la figura siguiente vemos dos ejemplos de esta sentencia.

<center>

![Funcionamiento de continue](../img/programacion/python/ejem_continue.png)  
*Funcionamiento de ```continue```*

</center>

## <FONT COLOR=#007575>**Imágenes**</font>
MicroPython nos ofrece muchas imágenes integradas para mostrar por pantalla y podemos crear efectos interesantes. Mediante la característica de autocompletar se nos van a mostrar todas las definidas que están listadas en la documentación oficial. Ya hemos visto como cargar una imagen, lo que puedo aconsejar en este momento es realizar el ejercicio de mostrar cada una de las disponibles para familiarizarnos con ellas.

Es perfectamente posible crar nuestras propias imágenes configurando cada Pixel o LED de la pantalla. También es posible crear animaciones con imágenes.

### <FONT COLOR=#AA0000>Imágenes DIY</font>
Crear nuestras propias imágenes va a resultar una tarea sencilla cuando conozcamos la información para hacerlo. Cada pixel (LED) de la pantalla se puede configurar con diez valores que pueden tomar un valor entre 0 (cero) y 9 (nueve). Cuando le damos valor 0 (cero) es decirle literalmente que el brillo es nulo y sin embargo cuando le damos el valor 9 (nueve) lo ponemos al máximo de brillo posible. Podemos jugar con todos los valores intermedios para crear niveles de brillo.

La forma mas sencilla de definir una imagen consiste en utilizar la *clase microbit.Image* para crearla a partir de una cadena o string que devuelva el pictograma. Es decir utilizando el comando *Image(string)* teniendo que constar de dígitos con los valores 0 a 9 indicados. Para verlo rapidamente hacemos el ejemplos de dibujar una X en relieve asignándola a una variable.

~~~python
mi_imagen_X = Image("90009:"
                    "06060:"
                    "00300:"
                    "06060:"
                    "90009")
~~~

Los dos puntos indican un salto de línea por lo que se puede usar el ASCII no imprimible "\n" que es precisamente eso, un salto de línea.

~~~python
mi_imagen_X = Image("90009\n"
                    "06060\n"
                    "00300\n"
                    "06060\n"
                    "90009")
~~~

Los valores de brillo dan la sensación de relieve de profundidas a la X.

En cualquier caso esto no se escribe normalmente así, salvo para hacer mas o menos un gráfico del pixelado, sino en una sola línea.

~~~python
mi_imagen_X = Image("90009\n06060\n00300\n06060\n90009")
~~~

Ahora parece mas elegante utilizar los dos puntos como indicador de salto de línea.

~~~python
mi_imagen_X = Image("90009:06060:00300:06060:90009")
~~~

En la imagen vemos el resultado de lo explicado.

<center>

![mi imagen de una X en relieve](../img/programacion/python/mi_X_relieve.png)  
*mi imagen de una X en relieve*

</center>

Este es el código creado:

~~~python
from microbit import * 
"""mi_imagen_X = Image("90009\n"
                       "06060\n"
                       "00300\n"
                       "06060\n"
                       "90009")"""
#mi_imagen_X = Image("90009\n06060\n00300\n06060\n90009")
mi_imagen_X = Image("90009:06060:00300:06060:90009")
display.show(mi_imagen_X)
~~~

### <FONT COLOR=#AA0000>Animar imágenes</font>
En micro:bit Python ya disponemos de un par de listas de imágenes incorporadas que se llaman

~~~python
Image.ALL_Clocks
Image.ALL_ARROWS
~~~

Estas dos ordenes hacen que MicroPython entienda que necesita mostrar cada imagen de la lista, una tras otra.

Cuando queremos mostrar en la pantalla una imagen se nos muestra la siguiente ayuda contextual:

<center>

![Ayuda contextual para display.show()](../img/programacion/python/ayuda_disp_show.png)  
*Ayuda contextual para display.show()*

</center>

donde nos indica claramente qie **image** puede ser una cadena, un número, una imagen o una lista de imágenes. Además aparecen las opciones que podemos configurar.

Con esta información crear un "reloj" que esté continuamente marcando cada hora es bastante sencillo, basta con poner el siguiente código y darle a simular.

~~~python
# Imports go at the top
from microbit import *
display.show(Image.ALL_CLOCKS, delay=400, loop=True)
~~~

En la animación vemos el funcionamiento de este "reloj".

<center>

!["Reloj" creado con display.show() y mostrar una lista](../img/programacion/python/reloj_lista.gif)  
*"Reloj" creado con display.show() y mostrar una lista*

</center>

Si cambiamos el reloj por las flechas veremos como van rotando flechas en ángulos de 45 grados.

<center>

![Flechas creado con display.show() y mostrar una lista](../img/programacion/python/flechas_lista.gif)  
*Flechas creado con display.show() y mostrar una lista*

</center>

Para animar nuestras propias imágenes tendremos que crear cada una sobre un lienzo de 5x5 pixeles y establecer las diferencias para crear la animación. Podemos crear tantas imágenes como creamos oportuno. Creamos una lista con todas las imágenes en el orden que se tienen que reproducir y ya podemos mostrar nuestra lista en la pantalla.

En la animación siguiente vemos un efecto creado de esta forma.

<center>

![Cortinilla animada](../img/programacion/python/cortinilla.gif)  
*Cortinilla animada*

</center>

Este es el código para crear la animación.

~~~python
# Imports go at the top
from microbit import *
display.clear()
cor1=Image("90000:90000:90000:90000:90000")
cor2=Image("79000:79000:79000:79000:79000")
cor3=Image("57900:57900:57900:57900:57900")
cor4=Image("35790:35790:35790:35790:35790")
cor5=Image("13579:13579:13579:13579:13579")
cor6=Image("01357:01357:01357:01357:01357")
cor7=Image("00135:00135:00135:00135:00135")
cor8=Image("00013:00013:00013:00013:00013")
cor9=Image("00001:00001:00001:00001:00001")
cor10=Image("00000:00000:00000:00000:00000")
todas_las_cortinas=[cor1,cor2,cor3,cor4,cor5,cor6,cor7,cor8,cor9,cor10]
display.show(todas_las_cortinas, delay=100, loop=True)
~~~

## <FONT COLOR=#007575>**Sentencia condicional ```if...else```**</font>
En Python hay tres formas de declaración de ```if...else```
>
1. Declaración ```if```
2. Declaración ```if...else```
3. Declaración ```if...elif...else```

1. Declaración ```if```. La sintaxix de esta declaración en Python tiene la forma siguiente:

~~~py
if condicion:
    # Cuerpo de la sentencia if

# Código después del if
~~~

Si el resultado de evaluar la condición es cierto (True o 1), el código en "Cuerpo de la sentencia if" y lo estará haciendo mientras se cumpla la condición.

En el momento que la condición sea evaluada como falsa (False o 0) el código en "Cuerpo de la sentencia if" se omite y  continua la ejecución del programa por "Código después del if". En la figura siguiente vemos la explicación de forma gráfica.

<center>

![Funcionamiento de la sentencia if](../img/programacion/python/f_if.png)  
*Funcionamiento de la sentencia ```if```*

</center>

2. Declaración ```if...else```. Una sentencia ```if``` puede tener de manera opcional una clausula ```else```. La sintaxix de esta declaración en Python tiene la forma siguiente:

~~~py
if condicion:
    # Bloque de sentencias si condicion es True

    else:
    # Bloque de sentencias si condicion es False
~~~

La sentencia se evalúa de la siguiente forma: Si ```condición``` es ```True``` se ejecuta el código dentro del ```if``` y el código dentro del ```else``` se omite. Si ```condición``` es ```False``` se ejecuta el código dentro del ```else``` y el código dentro del ```if``` se omite. Cuando finaliza bien la parte del ```if``` o bien la del ```else``` el programa continua con la siguiente sentencia.

En la figura siguiente vemos la explicación de forma gráfica.

<center>

![Funcionamiento de la sentencia if...else](../img/programacion/python/f_ifelse.png)  
*Funcionamiento de la sentencia ```if...else```*

</center>

3. Declaración ```if...elif...else```. La sentencia ```if...else``` se utiliza para ejecutar un bloque de código entre dos alternativas posibles. Sin embargo, si necesitamos elegir entre más de dos alternativas, entonces utilizamos la sentencia ```if...elif...else```. La sintaxis de la sentencia ```if...elif...else``` es:

~~~py
if condicion_1:
    # Bloque 1
elif condicion_2:
    #Bloque 2

    else:
    # Bloque 3
~~~

Se evalúa así: Si ```condicion_1``` es ```True```, se ejecuta Bloque 1. Si ```condicion_1``` es ```False```, se evalúa ```condicion_2```. Si ```condicion_2``` es ```True```, se ejecuta Bloque 2. Si ```condicion_2``` es ```False```, se ejecuta Bloque 3.

En la figura siguiente vemos la explicación de forma gráfica.

<center>

![Funcionamiento de la sentencia if...elif...else](../img/programacion/python/f_ifelifelse.png)  
*Funcionamiento de la sentencia ```if...elif...else```*

</center>

## <FONT COLOR=#007575>**Funciones en Python**</font>
En esta sección vamos a dar solamente una breve introducción a lo que son las funciones y los módulos en Python para estudiar dos funciones concretas definidas en MicroPhyton para micro:bit.

Una función es un bloque de código que realiza una tarea específica.

Supongamos que necesitas crear un programa para crear un círculo y colorearlo. Puedes crear dos funciones para resolver este problema:

* crear una función de círculo
* crear una función de color

Dividir un problema complejo en trozos más pequeños hace que nuestro programa sea fácil de entender y reutilizar.

Existen dos tipos de funciones en Python:

* **Standard library functions (Funciones de biblioteca estándar)**. Son funciones incorporadas en Python que están disponibles para su uso.
* **User-defined functions (Funciones definidas por el usuario)**. Podemos crear nuestras propias funciones para que cumplan con nuestros requisitos.

La sintaxis de una función es la siguiente:

~~~py
def nombre_funcion(argumentos):
    #Cuerpo de la función
    
    return
~~~

Donde,

* ```def``` es la palabra reservada para declarar una función
* ```nombre_funcion``` es el nombre que le damos a la función
* ```argumentos``` es el valor o valores pasados a la función
* ```return``` retorna un valor desde la función. Es opcional

Veamos un ejemplo sencillo que no manda parametros ni retorna nada.

~~~py
def saludo():
    print("Hola Mundo!")
    
saludo() #Llama a la función
print("Programa")
saludo()
print("Otra vez programa")
~~~
Va a generar como salida la cadena "Hola Mundo!" seguida de la cadena "Programa" seguida otra vez de "Hola Mundo!" y finaliza con "Otra vez programa".

Cuando se llama a la función, el control del programa pasa a la definición de la función, se ejecuta todo el código dentro de la función y despés el control del programa salta a la siguiente sentencia después de la llamada a la función.

Como ya se ha mencionado, una función también puede tener argumentos. Un argumento es un valor aceptado por una función. Cuando creamos una función con argumentos necesitamos pasar los correspondientes valores cuando la llamamos.

De forma genérica una función con argumentos tiene la siguiente sintaxis:

~~~py
def funcion(arg1, arg2, ar3,...):
    #Código

#Llamada a la función
funcion(valor1, valor2, valor3, ...)
#Código
~~~

Cuando llamamos a la función le pasamos los valores correspondiendo valor1 a arg1, valor2 a arg2 y así sucesivamente.

La llamada a la función se puede hacer mencionando el nombre del argumento, que es lo que se conoce como 'argumentos con nombre', siendo el código totalmente equivalente al anterior.

~~~py
funcion(arg1=valor1, arg2=valor2, arg3=valor3, ...)
~~~

Una función Python puede o no devolver un valor. Si queremos que nuestra función devuelva algún valor a una llamada realizada a función, utilizamos la sentencia ```return```.

En el ejemplo siguiente se llama a la función cuatro veces con valores diferentes.

~~~py
def cal_potencia(base, exponente):
    resultado = base ** exponente
    return resultado
    
#Llamadas a la función
print('Potencia =', cal_potencia(2,8))
print('Potencia =', cal_potencia(3,3))
print('Potencia =', cal_potencia(4,5))
print('Potencia =', cal_potencia(9,6))
~~~

El resultado es:

~~~py
Potencia = 256
Potencia = 27
Potencia = 1024
Potencia = 531441
~~~

En Python, las funciones de la biblioteca estándar son las funciones incorporadas que se pueden utilizar directamente en nuestro programa. Por ejemplo,

* ```print()```, imprime la cadena entre comillas
* ```sqrt()```, devuelve la raíz cuadrada de un número
* ```pow() ```, devuelve la potencia de un número

Estas funciones están definidas dentro de un módulo. Y, para utilizarlas debemos incluir dicho módulo en nuestro programa. Por ejemplo, ```sqrt()``` y ```pow()``` están definidos en el módulo ```math```. Para usar las funciones podemos hacer como en el ejemplo siguiente:

~~~py
import math #Carga el módulo math

raiz = math.sqrt(25)
print("La raiz cuadrada de 25 es ", raiz)

potencia = pow(2, 8)
print("2^8 =", potencia)
~~~

En el ejemplo la variable raiz contendrá el cálculo de la raiz cuadrada y se define por defecto como variable real o decimal y potencia contendrá el resultado de elevar a 8 el número 2. Los resultados obtenidos son:

~~~py
La raiz cuadrada de 25 es 5.0
2^8 = 256
~~~

Las principales ventajas de utilizar funciones son:

* **Código reutilizable**. Podemos llamar a la misma función tantas veces en nuestro programa como necesitemos, lo que hace que nuestro código sea reutilizable.
* **Código legible**. Las funciones nos ayudan a dividir nuestro código en trozos para que nuestro programa sea mas legible y fácil de entender.

## <FONT COLOR=#007575>**Módulos en Python**</font>
A medida que nuestro programa crece, puede contener muchas líneas de código. En lugar de poner todo en un solo archivo, podemos utilizar módulos para separar por funcionalidad los códigos en varios archivos. Esto hace que nuestro código quede organizado y sea más fácil de mantener.

Un módulo es un archivo que contiene código para realizar una tarea específica. Un módulo puede contener variables, funciones, clases, etc. Veamos un ejemplo, vamos a crear un módulo escribiendo algo como lo siguiente:

~~~py
#Definición del módulo suma

def sumar(a, b):

    resultado = a + b
    return resultado
~~~

Guardamos este programa en un archivo, por ejemplo ```modulo_sumar.py``` y tendremos definida una función de nombre ```sumar``` en ese módulo. La función recibe dos valores y devuelve la suma.

Cuando, en un programa diferente, queramos sumar dos números podemos importar la definición creada utilizando la palabra reservada ```import```. Para acceder a la función definida en el módulo tenemos que utilizar el operador ```.``` (punto). Se parece mucho a que el módulo es una clase y la función una instancia de esa clase.

~~~py
# Programa de sumas
import modulo_sumar

modulo_sumar.sumar(4, 5) #devolverá 9
~~~

Python tiene mas de 200 módulos estándar que pueden ser importados de la misma manera que importamos los módulos definidos por nosotros. En la documentación de Python en español encontramos la referencia a [La biblioteca estándar de Python](https://docs.python.org/es/3/library/index.html).

## <FONT COLOR=#007575>**Eventos para los botones**</font>
Si trabajamos con versiones anteriores a V2 solamente disponemos de los botones A, B y A+B, pero si tenemos una versión V2 también disponemos del botón táctil incorporado en el logo, aunque a todos los efectos este se considera un pin de entrada.

El logo no es tratado exactamente como un botón, sino como un pin de nombre logo. En el borde existen otros tres pines, los 0, 1 y 2. Por ello la forma de trabajar con el logo va a ser un poco diferente, como veremos en la actividad A04.

La diferencia fundamental, ademas de la forma, es que el logo es un sensor capacitivo y los pines son sensores resistivos. En la práctica esto significa que el logo funciona simplemente tocandolo y los pines necesitan cerrar el circuito con GND, por lo que para que funcionen como pulsador debemos tocar tanto el pinto como GND.

Si queremos que MicroPython reaccione a los eventos de pulsación de los botones, debemos ponerlo en un bucle infinito y comprobar si el botón ```is_pressed```.

* **Función ```is_pressed()```**

Para trabajar con los botones de la micro:bit tenemos disponibles funciones que se han cargado al importar el módulo ```microbit```. Estas funciones están basadas en la función genérica ```is_pressed()``` pensada para saber que tecla de un teclado se ha pulsado. Sin embargo, en el caso de MicroPython a para micro:bit a estos botones se les ha asignado un nombre a cada uno, ```button_a``` para el A y  ```button_b``` para el B, de manera que para usarlos se llama al botón y con el operador ```.``` a la función ```is_pressed()```. Por ejemplo, ```button_a.is_pressed()``` es el código encargado de saber si estamos pulsando el botón A y ```button_b.is_pressed()``` si lo es el B.

* **Función ```get_pressed()```**

Esta función retorna el total acumulado de pulsaciones de botones y restablece este total a cero antes de volver. Es decir, podemos capturar el número de veces que hemos pulsado un botón. El valor de retorno es un número, por lo que, para mostrarlo en la pantalla de LEDs hay que convertirlo en cadena con la función ```str()```.

* **Función ```was_pressed()```**

Devuelve ```True``` o ```False``` para indicar si se ha presionado el botón desde la última vez que se inicio el dispositivo o se llamó a este método. Llamar a este método borra el estado de que ha sido pulsado, de modo que el botón debe pulsarse de nuevo antes de que este método vuelva a retornar ```True```.

Vamos a hacer un ejemplo que aclarará mejor lo explicado. Se trata de crear un programa (le podremos de nombre Caritas_X) en el que mientras mantegamos pulsado el botón A se muestra una cara sonriente, si no se pulsa ningún botón se muestra una cara triste y si se pulsa el botón B la cara desaparece (se apagan todos los LEDs) y tras 2 segundos aparece una X que se va haciendo cada vez mas grande partiendo del punto central. Finalmente pasados otros 2 segundos el programa vuelve a empezar. El código es:

~~~py
from microbit import *
while True:
    while True:
        if button_a.is_pressed():
            display.show(Image.HAPPY)
        elif button_b.is_pressed():
            break
        else:
            display.show(Image.SAD)

    display.clear()
    sleep(2000)
    mi_X_peque = Image("00000:00000:00900:00000:0000")
    display.show(mi_X_peque)
    sleep(200)
    mi_X_media = Image("00000:09090:00900:09090:0000")
    display.show(mi_X_media)
    sleep(200)
    mi_X_grande = Image("90009:09090:00900:09090:90009")
    display.show(mi_X_grande)
    sleep(2000)
~~~

En la animación siguiente vemos como funciona

<center>

![Funcionamiento de Caritas_X](../img/programacion/python/f_caritas_X.gif)  
*Funcionamiento de Caritas_X*

</center>

Si observamos con cuidado apreciaremos que en algún momento se accionan los botones A y B pero los que aparecen en la parte inferior, debajo de la pantalla de simulación. Están al lado de un logotipo que indica que se pulsen con una flechita. Justo debajo de estos aparecen los citados del borde de placa y el logo junto a ellos, pues es tratado asi, como un pin, y además a su izquierda hay un candado cerrado indicativo de que no se está usando ninguno de ellos. En la imagen siguiente se ve mejor lo indicado.

<center>

![Control de acciones del simulador](../img/programacion/python/control_simu.png)  
*Control de acciones del simulador*

</center>

Vamos a crear otro ejemplo en el que se cuenten las veces que pulsamos el botón A o el botón B durante un tiempo de 3 segundo. El programa es el siguiente:

~~~py
from microbit import *

sleep(3000) #Espera de 3 segundos

#Convertimos número a cadena con str()
pulsado = str(button_b.get_presses())

display.show(pulsado)

# Por si hemos pulsado mas de 9 veces
display.scroll(pulsado)
~~~

En la 'Referencia' del compilador, dentro de Botones tenemos un ejemplo que nos indica el botón que hemos pulsado con cuatro opciones posibles, el A, el B, A o B y finalmente A y B. Animamos a cargarlos y probarlos para familiarizarnos todo lo posible con ellos.

## <FONT COLOR=#007575>**Pines de Entrada/salida**</font>

### <FONT COLOR=#AA0000>Digital</font>
Podemos utilizar los pines 0, 1 y 2 del borde de placa en modo digital tanto para leer su valor como para escribir o establecer su valor. Esto se representa con un "1" lógico (sin las comillas) si están activados o los queremos activar y un "0" lógico si están desactivados o los queremos desactivar.

Si queremos escribir en ellos los pines estarán actuando como salidas y tenemos que invocar al método ```write``` para hacerlo. Las sentencias, para un pin genérico "N" son:

~~~py
pinN.write_digital(1) #Salida en estado alto
pinN.write_digital(0) #Salida en estado bajo
~~~

También podemos conectar, por ejemplo un interruptor o botón pulsador al pin (veremos como hacerlo en la siguiente actividad) y comprobar si el interruptor está abierto (0) o cerrado (1). En este caso los pines estarán configurados como entradas y la lectura de su estado se obtiene invocando el método ```read```.  Las sentencias, para un pin genérico "N" son:

~~~py
pinN.read_digital() #Devuelve el estado 0 o 1 del pin N
~~~

***Nunca se conecta nada a los pines con un voltaje superior a 3v porque se puede dañar la micro:bit.***

### <FONT COLOR=#AA0000>Analógica</font>
Podemos utilizar los pines 0, 1 y 2 del borde de placa en modo analógico tanto para leer su valor como para escribir o establecer su valor. Esto significa que en lugar de estar activos o inactivos (0 o 1), varían su valor entre 0 y 1023.

Si queremos escribir en ellos los pines estarán actuando como salidas y tenemos que invocar al método ```write``` para hacerlo. La sentencia, para un pin genérico "N" es:

~~~py
pinN.write_analog(valor) #valor puede estar entre 0 y 1023
~~~

Si conectamos sensores o actuadores analógicos a los pines podemos leer su valor invocando a ```read```. La sentencia, para un pin genérico "N" es:

~~~py
pinN.read_analog(valor) #valor puede estar entre 0 y 1023
~~~
