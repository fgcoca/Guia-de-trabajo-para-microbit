# <FONT COLOR=#8B008B>MakeCode</font>
De manera muy resumida lo que haremos en esta sección es:

* Describir los bloques y conceptos relacionados.
* Incluiremos esquemas si resultan necesarios.

Se explican los bloques utilizados de los menús de bloques. Referencia a **micro:bit reference** [The micro:bit APIs](https://makecode.microbit.org/reference).

## <FONT COLOR=#007575>**Comentarios**</font>
Todo lenguaje de programación contempla la posibilidad de realizar comentarios en el código para que sirvan de aclaración de para que sirve cada bloque en el programa, en especial en alguna parte que transcurrido un tiempo nos resulte complicada de entender.

En MakeCode la forma de hacer comentarios es siempre sobre un bloque, así que si Si necesitamos añadir un comentario a un bloque desplegamos las opciones del bloque pinchando con el botón derecho y añadimos un comentario pinchando en la entrada 'añadir comentario'. Esto hará que aparezca, en la esquina superior izquierda del bloque, un pequeño icono con forma de hoja escrita. Si pulsamos sobre este icono se despliega un pequeño editor, dimensionable y movible, donde podemos escribir nuestro comentario. En este editor hay un símbolo de papelera que elimina el comentario actual. Esta opción está disponible también en el menú contextual, lógicamente si se ha creado un comentario. En la animación siguiente vemos el funcionamiento.

<center>

![Comentarios](../img/programacion/mkcode/coment.gif)  
*Comentarios*

</center>

## <FONT COLOR=#007575>**Básico**</font>
En este grupo tenemos acceso a la funcionalidad básica de la micro:bit.

* **al iniciar**. Se trata del bloque de la imagen y es un bloque que se ejecuta una sola vez cuando se inicia la micro:bit. Es uno de los dos bloques que aparecen al principio cuando escogemos *Restablecer* o creamos un nuevo proyecto desde *Mis proyectos*.

<center>

![Bloque 'al iniciar'](../img/programacion/mkcode/B_al_iniciar.png)  
*Bloque 'al iniciar'*

</center>

* **para siempre**. Se trata del bloque de la imagen y es un bloque que se ejecuta de manera infinita. Es el otro de los dos bloques que aparecen al principio cuando escogemos *Restablecer* o creamos un nuevo proyecto desde *Mis proyectos*.

<center>

![Bloque 'para siempre'](../img/programacion/mkcode/B_para_siempre.png)  
*Bloque 'para siempre'*

</center>

* **mostrar cadena**. Muestra la cadena de texto en la pantalla caracter a caracter. En la imagen la palabra es **Hello**.

<center>

![Bloque 'mostrar cadena'](../img/programacion/mkcode/B_mostrar_cad.png)  
*Bloque 'mostrar cadena'*

</center>

* **mostrar icono**. Dibuja el icono seleccionado en la pantalla.

<center>

![Bloque 'mostrar icono'](../img/programacion/mkcode/B_mostrar_icon.png)  
*Bloque 'mostrar icono'*

</center>

* **borrar la pantalla**. Apaga todos los LEDs.

<center>

![Bloque 'borrar la pantalla'](../img/programacion/mkcode/B_borra_pant.png)  
*Bloque 'borrar la pantalla'*

</center>

* **pausa (ms)**. Detiene la ejecución del programa el tiempo establecido en milisegundos.

<center>

![Bloque 'pausa (ms)'](../img/programacion/mkcode/B_pausa_ms.png)  
*Bloque 'pausa (ms)'*

</center>

## <FONT COLOR=#007575>**Pantalla LED**</font>
Control de la pantalla LED.

* **ajustar brillo**. Configura el brillo de la pantalla desde 0 (apagada) a 255 (máximo brillo). Los bloques de pantalla posteriores a este tendrán el brillo establecido hasta que no se cambien el valor a otro distinto.

<center>

![Bloque 'ajustar brillo'](../img/programacion/mkcode/B_brillo.png)  
*Bloque 'ajustar brillo'*

</center>

* **graficar x,y,brillo**. Enciende el LED indicado en la coordenada x,y con el brillo especificado. La coordenadas x es la horizontal y la y es la vertical. La coordenada 0,0 es la esquina superior ezquierda, la 0,4 es la derecha, la 4,0 es la inferior izquierda y la 4,4 la inferior derecha.

<center>

![Bloque 'graficar x,y,brillo'](../img/programacion/mkcode/B_graf_xy.png)  
*Bloque 'graficar x,y,brillo'*

</center>

## <FONT COLOR=#007575>**Arrays o arreglos**</font>
Se van a utilizar para agregar, eliminar y sustituir elementos en listas. En MakeCode las listas se nombran indistintamente como array, matriz o lista y tienen su propio menú de bloques que es visible cuando desplegamos 'Avanzado'. Los bloques existentes están clasificados en los siguientes grupos:

1. **Create**
2. **Leer**
3. **Modificar**
4. **Operaciones**

Describiremos estos grupos de forma somera porque esta es suficiente para entender lo que hace el bloque. No obstante, algunos se describen de manera mas explicita.

### <FONT COLOR=#AA0000>Create</font>

* **fijar 'nn' a**. Le da a la variable el valor de la entrada, para valores numéricos.
* **fijar 'tt' a**. Le da a la variable el valor de la entrada, para texto.
* **matriz vacia**. Crea una lista con los elementos que introduzcamos con el '+'.

### <FONT COLOR=#AA0000>Leer</font>

* **longitud del arreglo**. Devuelve el número de elementos de una lista.
* **obtener el valor en 'x'**. Obtiene el valor del elemento 'x'.
* **eliminar el valor en 'x'**. Elimina el elemento 'x' de la lista.
* **obtener y eliminar el último valor de (```pop```)**. Elimina y devuelve el último elemento de una matriz. Se elimina el último elemento de la matriz, por lo que la matriz se reduce en un elemento.
* **obtener y eliminar el primer valor de (```shift```)**. Elimina y devuelve el primer elemento de una matriz. Se elimina el primer elemento de la matriz, por lo que la matriz se reduce en un elemento.
* **obtener valor aleatorio**. Devuelve un valor al azar de la matriz.

### <FONT COLOR=#AA0000>Modificar</font>

* **establecer el valor en 'x' a 'nn'**. Estable el valor del elemento 'x' al valor indicado en 'nn'.
* **añadir valor 'nn' al final (```push```)**. Añade un nuevo elemento al final de una matriz.
* **eliminar el último valor de**. Elimina el último elemento de la matriz y lo devuelve.
* **eliminar el primer valor de**. Elimina el primer elemento de la matriz y lo devuelve.
* **insertar 'nn' al principio (```unshift```)**. Añadir un elemento al principio de una matriz y devolver la nueva longitud de la matriz.
* **insertar en 'x' valor 'nn' (```insertAt```)**. Inserta el valor 'nn' en la posición espeífica indicada por 'x' aumentando la longitud del array en uno. El elemento se agrega a la matriz en la posición que indiquemos. Si ya hay un elemento en esa posición, entonces él y todos los elementos posteriores se desplazan a la posición superior siguiente.
* **eliminar valor en 'x' (```removeAt```)**. Elimina el elemento que hay en la posición 'x'. El tamaño de la matriz se reduce en uno. El elemento se elimina de la matriz en la posición que indiquemos. Todos los demás elementos posteriores se desplazan hacia abajo a la posición inferior siguiente.

### <FONT COLOR=#AA0000>Operaciones</font>

* **bloque encontrar indice de (```IndexOf```)**. Devuelve la posición o índice de la primera aparición de un valor en una matriz. Devuelve un número, que es la posición en la matriz del elemento. El resultado es -1 si no se encuentra ninguna coincidencia.
* **invertir (```reverse```)**. Invertir los elementos de una matriz.

## <FONT COLOR=#007575>**Variables**</font>
Cuando vamos a utilizar bucles, estos siempre llevan asociada una variable, y por eso debemos aprender a gestionar el tema de las variables en MakeCode. Las variables tienen su propio menú y es relativamente sencillo de usar. Como ya se ha dicho, una variable es un espacio en la memoria donde el programa puede almacenar valores. El sistema nos permite asignarles un nombre simbólico como por ejemplo “temperatura”, “velocidad”, ”estado”,… para facilitar su uso.

Cuando accedemos al menú 'Variables' por primera vez y si no hemos pues ningún bloque en el área de programa, el aspecto del menú es el siguiente:

<center>

![Variables en MakeCode](../img/programacion/mkcode/MC/MC01.png)  
*Variables en MakeCode*

</center>

Veamos como funciona la creación de una variable, cambiarle el nombre, eliminarla y demás tareas que podemos hacer con ellas. En la animación siguiente vemos el proceso de crear y poner nombre a una variable. Vemos que al hacer clic en el botón se abre una ventana de diálogo donde nos pide el nombre, que tecleamos según las reglas establecidas, y que al hacer clic en 'Aceptar' se nos crean tres bloques, dos para trabajar con la variable creada y uno que es la propia variable, todos ellos con el nombre que hemos puesto a esa variable.

<center>

![Creación de una variable en MakeCode](../img/programacion/mkcode/MC/MC02.gif)  
*Creación de una variable en MakeCode*

</center>

El bloque 'fijar' sirve para inicializar la variable al valor especificado, el bloque 'cambiar' es el equivalente al operador '+=' con el incremento que establezcamos en 'por' y el último bloque es el valor de la variable.

Al final de la animación también vemos que al hacer clic en la flechita de cualquiera de los bloques se despliega un menú en el que aparece la variable, la opción de crear otra nueva, renombrarla o borrar la variable que está seleccionada en ese momento. En la animación siguiente vemos estos aspectos en funcionamiento.

<center>

![Trabajo con el menú desplegable en una variable en MakeCode](../img/programacion/mkcode/MC/MC03.gif)  
*Trabajo con el menú desplegable en una variable en MakeCode*

</center>

Cuando pasamos por el menú de bloques vemos que 'fijar' y 'cambiar' no se vuelven a crear cuando creamos nuevas variables ya que están todas en el desplegable y lo único que tenemos que hacer es seleccionarlas. Si se crea, en cambio, un bloque para el contenido de cada variable. También vemos que si eliminamos una variable que está en uso en varios sitios se elimina, preva advertencia, de todos ellos.

Ahora bien, la variables como tal se eliminan de la zona de programa pero no del menú 'Variables, donde siguen estando disponibles hasta que las eliminemos, tarea que solamente es posible hacer desde alguno de los bloques situado en la zona de programa.

## <FONT COLOR=#007575>**Bucles**</font>

### <FONT COLOR=#AA0000>Bloque for</font>
Son bloques que repiten el código asociado un número determinado de veces, Lo pueden hacer utilizando una variable como índice o estableciendo el número exacto de veces.

El aspecto del bloque para recorrer con una variable lo vemos en la imagen siguiente:

<center>

![Bloque for en MakeCode](../img/programacion/mkcode/MC/MC04.png)  
*Bloque for en MakeCode*

</center>

Cuando llevamos el bloque a la zona de programa se creará una variable index, salvo que esta ya exista. Un bloque como el siguiente creará un contador con la variable i desde 0 hasta 4 y mostrará los números 0 al 9 uno tras otro en la pantalla LED.

<center>

![Contador de 0 a 9](../img/programacion/mkcode/MC/MC05.png)  
*Contador de 0 a 9*

</center>

Una variedad de este bloque la tenemos en el bloque 'repetir' para el número de veces que indiquemos, que tiene el aspecto que vemos en la figura siguiente.

<center>

![Bloque repetir nn veces](../img/programacion/mkcode/MC/MC06.png)  
*Bloque repetir nn veces*

</center>

En el ejemplo siguiente, cuando se inicia el dispositivo, se producen tres efectos de latido de un corazón.

<center>

![Ejemplo de uso del bloque repetir nn veces](../img/programacion/mkcode/MC/MC07.png)  
*Ejemplo de uso del bloque repetir nn veces*

</center>

Otro bloque que utiliza el bucle for es el que vemos en la imagen siguiente, un bloque pensado para repetir el código para cada valor de los contenidos en una lista.

<center>

![Bucle for para elementos de una lista](../img/programacion/mkcode/MC/MC08.png)  
*Bucle for para elementos de una lista*

</center>

En la imagen siguiente vemos un programa que utiliza este bloque. Hemos creado una lista aleatoria de valores y el programa lo que hace es encontrar y mostrar el mayor de ellos. El funcionamiento del programa lo leemos asi: se crea una variable ```mayor``` para guardar el valor del elemento de la lista de mayor valor, la matriz le hemos dejado el nombre ```lista``` y para recorrerla se utiliza la variable ```valor```. El condicional (los veremos en una actividad posterior) va comprobando si ```valor > mayor``` y mientras sea cierto se guarda en ```mayor``` el ```valor``` leido y si no es cierto se continúa con el siguiente elemento de la lista. Una vez finalizado el condicional se mestra la cadena con la variable ```mayor```.

<center>

![Ejemplo de bucle for para elementos de una lista](../img/programacion/mkcode/MC/MC09.png)  
*Ejemplo de bucle for para elementos de una lista*

</center>

### <FONT COLOR=#AA0000>Bloque while</font>
Se trata de un bloque que repite su bloque de código mientras la condición sea cierta (```True```). Su aspecto lo vemos en la imagen siguiente.

<center>

![Bucle while](../img/programacion/mkcode/MC/MC10.png)  
*Bucle while*

</center>

El bucle while tiene una condición que se evalúa con un valor ```booleano```. La condición se comprueba antes de que se ejecute ningún código. Lo que significa que si la condición es falsa la primera vez que se evalúa, el código dentro del bucle no se ejecuta núnca.

Con el bloque tal cual es solamente podemos establecer la condición como ```True``` o ```False```, lo que es muy poca cosa. Es evidente que podrá tener mucha mas potencia si recurrimos a condiciones mas complejas y utilizamos los operadores. Este apartado no lo vamos a estudiar en este momento, pero si diremos que estos bloques están en el menú 'Lógica' y su funcionamiento es el mismo que en visto en [Python -> Introducción](../guias/intro.md).

Como ejemplo vamos a ver como dibujar una línea diagonal en los LEDs [(0,0) - (1,1) - (2,2) - (3,3) - (4,4) y (5,5)] de la pantalla. En la imagen vemos el programa final, donde observamos que la condición va a ser cierta hasta que index alcance el valor 4, por lo que se va a ir encendiendo cada LED a intervalos de un segundo. Esto solamente va a ocurrir cuando se inicia el disposiivo, aunque en este ejemplo concreto esto no tiene importancia.

<center>

![Programa bucle while](../img/programacion/mkcode/MC/MC11.png)  
*Programa bucle while*

</center>

### <FONT COLOR=#AA0000>Bloque cada 'nn' ms</font>
Repite el código en segundo plano de forma contnuada en el intervalo de tiempo que se indique. Establecemos la cantidad de tiempo que el bucle espera antes de que el código en su interior se ejecute de nuevo. Esto es similar a un bucle "forever" (por siempre), en el sentido de que se ejecuta continuamente, excepto que hay un intervalo de tiempo establecido para esperar antes de que el bucle se ejecute la próxima vez. El bloque es muy útil si, por ejemplo, queremos estar comprobando cada cierto tiempo si ocurre un evento, como pulsar una tecla, escuchar un sonido, etc.

En la imagen siguiente vemos el aspecto que tiene el bloque.

<center>

![Bloque cada 'nn' ms](../img/programacion/mkcode/MC/MC12.png)  
*Bloque cada 'nn' ms*

</center>

### <FONT COLOR=#AA0000>Bloques salir y continuar </font>
Son los bloques equivalentes a las sentencias ```break``` y ```continue``` en MicroPython y funcionan exactamente igual, es decir, el bloque 'salir' permite salir de un bucle de forma inmediata y el bloque 'continuar' sirve para saltarse la iteración actual del bucle.

Los bloques tienen el aspecto que vemos en la imagen.

<center>

![```break``` y ```continue```](../img/programacion/mkcode/MC/MC13.png)  
*```break``` y ```continue```*

</center>

## <FONT COLOR=#007575>**Operadores de comparación y booleanos**</font>
Como sabemos un valor booleano solamente puede tomar uno de dos valores posibles: ```True (verdadero)``` o ```False (falso)```. Estos bloques los encontramos en la entrada 'Lógica' y son:

<center>

![Valores booleanos](../img/programacion/mkcode/1/valores.png)  
*Valores booleanos*

</center>

Los dos bloques existen de forma separada, pero cada uno de ellos puede adoptar el valor contrario al que muestra por defecto seleccionandolo con la flechita.

Los operadores booleanos u operadores lógicos son AND, OR y NOT y son operadores que a partir de valores de entrada booleanos crean otro valor también booleano. Estos bloques también los encontramos en la entrada 'Lógica' y son:

<center>

![Operadores booleanos](../img/programacion/mkcode/1/operadores_bool.png)  
*Operadores booleanos*

</center>

A continuación vemos una serie de bloques con operadores que satisfacen la condición.

<center>

![Operadores booleanos](../img/programacion/mkcode/1/operadores_b.png)  
*Operadores booleanos*

</center>

Tanto los valores booleanos como los operadores se usan con instrucciones ```if``` o ```while``` para determinar qué código se ejecutará a continuación. Por ejemplo:

<center>

![Bucle ```while``` con una condición](../img/programacion/mkcode/1/bucle_while.png)  
*Bucle ```while``` con una condición*

</center>

En el siguiente ejemplo se utilizan operadores booleanos en el bucle.

<center>

![Bucle ```while``` con una condición y operadores booleanos](../img/programacion/mkcode/1/buc_while.png)  
*Bucle ```while``` con una condición y operadores booleanos*

</center>

## <FONT COLOR=#007575>**Sentencia condicional ```if...elif...else```**</font>

* **```if```**. Ejecuta código dependiendo de si una condición booleana es verdadera o falsa. El código dentro del bloque ```if``` sólo se ejecuta cuando el bloque ```condición``` es verdadero.

<center>

![Condicional ```if```](../img/programacion/mkcode/1/if.png)  
*Condicional ```if```*

</center>

Se pueden comparar variables con valores o variables con variables, para una condición verdadera o falsa.

* **```else```**. Si necesitamos que se ejecute algún otro código cuando la condición del ```if``` no sea verdadera, lo ponemos en un área de bloque adicional llamada ```else``` (si no).

<center>

![Condicional ```if...else```](../img/programacion/mkcode/1/if_else.png)  
*Condicional ```if...else```*

</center>

Un condicional como el siguiente se podría leer como: "``si`` tengo dinero por encima de una cantidad, ```entonces``` estoy feliz y ```si no``` estoy triste.

<center>

![Condicional ```if...else```](../img/programacion/mkcode/1/ifelse.png)  
*Condicional ```if...else```*

</center>

Cambiando el valor asignado a dinero vemos el funcionamiento.

La clausula ```else``` se añade al condicional ```if``` haciendo clic en el signo '+'.

* **```if...else if```**. Condición ```if``` que si resulta falsa se evalua una nueva condición puesta en ```elif```. Otra acción condicional es añadir un ```if``` a un ```else``` para obtener un ```else if```. Funciona así

<center>

![Condicional ```if...else if```](../img/programacion/mkcode/1/ifelseif.png)  
*Condicional ```if...else if```*

</center>

Hacemos clic en el símbolo más '+' para añadir secciones ```else``` o ```else if``` al bloque ```if``` actual.

## <FONT COLOR=#007575>**Texto**</font>
Si expandimos el menú 'Avanzado' nos encontraremos con una entrada 'Texto' que vamos a describir en esta actividad.

* ![](../img/programacion/mkcode/T/t1.png) Una letra, palabra o línea de texto que puede contener letras, números y caracteres.
* ![](../img/programacion/mkcode/T/t2.png) Devuelve el número de caracteres de la cadena de texto.
* ![](../img/programacion/mkcode/T/t3.png) Añade una cadena de texto a otra para crear una cadena mas larga. Se pueden añadir mas cadenas.
* ![](../img/programacion/mkcode/T/t4.png) Convierte un texto que sólo tiene caracteres numéricos en un valor numérico de coma flotante. Se puede convertir una cadena de texto con caracteres numéricos en un valor real de coma flotante. El texto debe tener sólo caracteres numéricos. Aunque también puede incluir los símbolos '-' y '.'. Si el texto tiene otros caracteres, como "-5.8g5u7", sólo se devuelve -5.8 ya que es el mejor intento de conversión a un número. Por lo tanto, hay que no mezclar caracteres numéricos con letras u otros símbolos.

**Potencias de 10**. Si la cadena de texto tiene la letra 'e' después de los caracteres numéricos y luego algunos caracteres numéricos más como "2e4", entonces los caracteres numéricos después de la 'e' son un exponente de 10. Esto significa que una cadena con "7.5e2" se convierte en el valor de 750 cuando se convierte a un número de coma flotante. Esto se debe a que el 2 después de la 'e' indica 10², lo que equivale a ```10 * 10 =  100```. El valor resultante es entonces 7.5 * 100 que es igual a 750. En el siguiente ejemplo se toman los primeros dígitos de PI de la frase "pi vale 3.141592" y los convierte en un número.

<center>

![Extraer PI de una cadena](../img/programacion/mkcode/T/t4ejem.png)  
*Extraer PI de una cadena*

</center>

[Descargar el programa](../ejemplos/microbit-PI.hex)

* ![](../img/programacion/mkcode/T/t5.png) Divide una cadena en cadenas más pequeñas utilizando un caracter (una cadena) de separación para dividir la cadena más grande.
* ![](../img/programacion/mkcode/T/t6.png) Determina si una cadena contiene los caracteres de una cadena especificada.
* ![](../img/programacion/mkcode/T/t7.png) Obtiene la posición (índice) de la primera aparición de un valor especificado en una cadena.
* ![](../img/programacion/mkcode/T/t8.png) Determina si una cadena de texto contiene caracteres o no. TODO
* ![](../img/programacion/mkcode/T/t9.png) Toma una parte de la cadena "this" para hacer una cadena más pequeña (subcadena). * Si una cadena tiene una parte que está copiada de otra cadena, se llama subcadena. Se puede crear una nueva cadena que sólo contenga la palabra "aquí" a partir de una cadena mayor que diga "¡Hola, estamos aquí!". Para ello, la subcadena se copia desde la posición de carácter 15 en la primera cadena y se copian 4 caracteres. Se hace así: ![](../img/actividades/A03/T/t9b.png). En el ejemplo se copian los sustantivos de la frase en dos cadenas más pequeñas.

<center>

![Extraer de cadena a subcadenas](../img/programacion/mkcode/T/t9ejem.png)  
*Extraer de cadena a subcadenas*

</center>

[Descargar el programa](../ejemplos/microbit-subcadenas_de_cadena.hex)

* ![](../img/programacion/mkcode/T/t10.png) Se comparan dos cadenas de texto en función de los caracteres que aparecen en primer lugar. Dos cadenas se comparan en función del orden de sus caracteres. Si la cadena "A" vale "111" será menor que una cadena con "512". Una cadena con "Everything (Todo)" es menor que "Nothing (Nada)" porque la 'N' viene después de la 'E' en el alfabeto. La cadena "abcdefg" es mayor que "abcdefa". Son casi iguales, pero la última letra de la segunda cadena es menor que la última letra de la primera. Esto hace que toda la segunda cadena se compare como menor. En bloques, la comparación de estas cadenas tiene el siguiente aspecto:

<center>

![Comparar cadenas](../img/programacion/mkcode/T/t10b.png)  
*Comparar cadenas*

</center>

* ![](../img/programacion/mkcode/T/t11.png) Obtiene un carácter (letra, número o símbolo) de un lugar de la cadena de texto. Podemos averiguar qué carácter se encuentra en cualquier lugar de un texto. Puedes tener un texto que diga "Hello there!". El carácter en la posición 6 es 't'. La palabra "Hello" más el espacio tienen las posiciones 0 - 5, así que, 't' está en la posición 6. Para obtener el carácter en esta posición, la letra 't', se podría usar un bloque como este:

<center>

![Extraer caracter de una cadena](../img/programacion/mkcode/T/t11b.png)  
*Extraer caracter de una cadena*

</center>

* ![](../img/programacion/mkcode/T/t12.png) Convierte el valor de cualquier tipo de dato a una cadena de texto. El siguiente ejemplo convierte un valor booleano y un valor numérico en cadenas y las une en una cadena o frase.

<center>

![Convertir valores booleanos y numéricos en cadena](../img/programacion/mkcode/T/t12ejem.png)  
*Convertir valores booleanos y numéricos en cadena*

</center>

[Descargar el programa](../ejemplos/microbit-convertir_a_cadena.hex)

* ![](../img/programacion/mkcode/T/t13.png) Hacer que una cadena de un caracter sea representada a partir del código numérico que le asignemos. Al igual que el código ASCII es un juego de caracteres que asigna un valor a cada uno de ellos, nosotros podemos crear nuestro propio código asignándole un código con este bloque. Por ejemplo, hacer que la letra B sea: ![](../img/actividades/A03/T/t13b.png)

## <FONT COLOR=#007575>**Bloques de 'Entrada' para los botones**</font>
Cuando presionamos los botones A y/o B ocurre un evento (se ha presionado un botón). Este tipo de acción se considera una entrada a la microbit y tenemos bloques para manejarlo.

* **al presionar el botón**

Presionar un botón inicia un manejador de eventos, que es una parte del programa que se ejecutará cuando ocurra algo, como por ejemplo,  cuando se pulsa un botón. Este manejador funciona cuando se pulsa el botón A o B, o A y B al mismo tiempo.Cuando estemos utilizando esta función en un navegador, pulsaremos los botones de la pantalla en lugar de los del micro:bit.

* Para el botón **A** o **B**: Este manejador de evento funciona cuando el botón se pulsa y se suelta en menos de un segundo.
* Para **A** y **B** juntos: Este manejador funciona cuando A y B son presionados simultanemente. Disponemos de un segundo y medio desde que pulsamos el primer botón hasta que pulsamos el segúndo para que se consideren ambos pulsados a la vez.

<center>

![Bloque 'Al presionar el botón...'](../img/programacion/mkcode/1/al_pres_bot.png)  
*Bloque 'Al presionar el botón...'*

</center>

En el siguiente ejemplo se cuenta cuántas veces se pulsa el botón A. Cada vez que se pulsa el botón, la pantalla LED muestra la variable de recuento que cada vez será mayor.

<center>

![Contar pulsaciones de A](../img/programacion/mkcode/1/cuenta_a.png)

*Contar pulsaciones de A*

</center>

[Descargar el programa](../ejemplos/microbit-cuenta_puls_A.hex)

En el ejemplo siguiente se simula un dado mostrando un número del 1 al 6 cuando pulsamos el botón B. En el programa se utiliza el bloque de generación de número aleatorios entre dos valores dados que podemos encontrar en el menú 'Matemáticas'.

<center>

![Dado](../img/programacion/mkcode/1/dado.png)

*Dado*

</center>

[Descargar el programa](../ejemplos/microbit-dado_B.hex)

* **botón A o B presionado**

El bloque siguiente comprueba si se está pulsando un botón en ese momento.

<center>

![Se ha presionado el botón](../img/programacion/mkcode/1/pres_bot.png)

*Se ha presionado el botón*

</center>

Un sencillo ejemplo nos aclara como funciona el bloque.

<center>

![Botón A presionado](../img/programacion/mkcode/1/b_a.png)

*Botón A presionado*

</center>

[Descargar el programa](../ejemplos/microbit-pulsado_A.hex)

* **al pulsar el logotipo <font color=#FF0000> (solo en versiones V2)</font color>**

El logo de **micro:bit V2** actúa como un botón táctil, por lo que es un actuador de entrada que cuando lo pulsamos (tocamos) se ejecuta su código y cuando lo soltamos (no lo tocamos) deja de hacerlo.

<center>

![Botón táctil](../img/programacion/mkcode/1/b_tactil.png)

*Botón táctil*

</center>

El bloque funciona solamente con micro:bit V2 y si lo usamos con una placa V1 nos generará el código de error **927** en la pantalla.

* **el logotipo está pulsado <font color=#FF0000> (solo en versiones V2)</font color>**

Comprueba si se está pulsando el logotipo de micro:bit. Utilizamos el valor booleano del estado de la pulsación del logo para tomar una decisión lógica en el programa.

El ejemplo muestra una u otra imagen en función de si se ha pulsado el logo o no.

<center>

![logo presionado](../img/programacion/mkcode/1/logo_pre.png)

*Logo presionado*

</center>

[Descargar el programa](../ejemplos/microbit-pulsado_logo.hex)

## <FONT COLOR=#007575>**Pines**</font>
MakeCode dispone de bloques para controlar la corriente en los pines tanto para señales analógicas como digitales, servos, dispositivos i2c,...

* ![](../img/programacion/mkcode/pines/b/b1.png). Lee el valor de una señal digital (0 o 1) desde el pin de la placa micro:bit. Los pines disponibles para el bloque son:

<center>

![Pines para lectura digital](../img/programacion/mkcode/pines/p1.png)

*Pines para lectura digital*

</center>

* ![](../img/programacion/mkcode/pines/b/b2.png). Escribe el valor de una señal digital (0 o 1) en un pin de la placa micro:bit. Los pines disponibles para escritura digital son los mismos que para lectura digital.
* ![](../img/programacion/mkcode/pines/b/b3.png). Lee una señal analógica (0 a 1023) desde el pin indicado. Los pines disponibles son:

<center>

![Pines para escritura digital](../img/programacion/mkcode/pines/p2.png)

*Pines para escritura digital*

</center>

* ![](../img/programacion/mkcode/pines/b/b4.png). Escribe una señal analógica (0 a 1023) en el pin indicado. Los pines disponibles son los indicados para la lectura analógica.
* ![](../img/programacion/mkcode/pines/b/b5.png). Configura el periodo de la modulación por anchura de pulso o PWM de la salida analógica en microsegundos. Antes de llamar a esta función debemos configurar el pin indicado como analógico. Tenemos los mismo pines disponibles que para la lectura y escritura.
* El bloque siguiente es un bloque de lo que se conoce como mapeo. El mapeo consiste en reasignar un valor especificado dentro de un rango a otro rango diferente. Es com si hacemos un cambio de escala de los valores. La función no limita los valores de los rangos, porque los valores fuera de rango a veces están previstos y son útiles. Si necesitamos limitar un rango, podemos utilizar la función 'restringir' de 'Matemáticas'.

<center>

![](../img/programacion/mkcode/pines/b/b6.png)

</center>

Por ejemplo, el programa siguiente cambia los valores analógicos recibidos en el pin P0 de absolutos a porcentaje.

<center>

![Mapeo de valores](../img/programacion/mkcode/pines/p3.png)

*Mapeo de valores*

</center>

* El bloque siguiente configura el pin indicado como una entrada digital y genera un evento cuando el pin es tocado, tanto alto como bajo. Este bloque no se puede simular y requiere hardware real para probarlo.

<center>

![](../img/programacion/mkcode/pines/b/b7.png)

</center>

A continuación vemos los pines que se pueden configurar en el bloque.

<center>

![Pines para el bloque cuando el pin nn es pulsado](../img/programacion/mkcode/pines/p4.png)

*Pines para el bloque cuando el pin nn es pulsado*

</center>

* ![](../img/programacion/mkcode/pines/b/b8.png). Obtiene la duración del pulso en microsegundos.
* ![](../img/programacion/mkcode/pines/b/b9.png). Devuelve la duración de un pulso en microsegundos.
* ![](../img/programacion/mkcode/pines/b/b10.png). Configura el pull del pin indicado. Hay muchos pines que se pueden configurar con pull-up. Por ejemplo, podemos establecer el valor de tensión de un pin a 3.3V o un "1" lógico.
* ![](../img/programacion/mkcode/pines/b/b11.png). Emite una señal PWM al pin actual.
* ![](../img/programacion/mkcode/pines/b/b12.png). Establece el pin que se utiliza para un tono musical analógico.