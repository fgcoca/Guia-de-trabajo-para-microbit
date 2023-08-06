# <FONT COLOR=#8B008B>Componentes discretos</font>
Se describen brevemente las características y principio de funcionamiento de los componentes básicos para construir circuitos que se montan para pruebas.

## <FONT COLOR=#007575>**Cables y conectores**</font>
En electrónica se utilizan multitud de cables y conectores especializados por características y por aplicación. Para lo que nos interesa existen unos componentes básicos conocidos como puentes, jumpers o cables dupont que están diseñados para interconectar componentes mediante la inserción de sus dos terminales.

Estos cables utilizan en sus extremos (lo llevan crimpado) o bien conectores macho (Male) o bien hembra (Female), por lo que se pueden clasificar en los tres tipos siguientes, que se comercializan en diferentes colores y longitudes.

<center>

|Conexiones|Cable|
|:-:|:-:|
|macho-macho (M/M)|![](../img/conceptos/discretos/mm.png)|
|hembra/hembra (F/F)|![](../img/conceptos/discretos/ff.png)|
|macho/hembra (M/F)|![](../img/conceptos/discretos/mf.png)|

</center>

## <FONT COLOR=#007575>**Protoboard**</font>
También conocida como breadboard es una placa con multitud de agujeros interconectados de una determinada manera formando grupos de conexiones. Permiten montar de forma rápida circuitos mas o menos sencillos. Existen de muchos tamaños diferentes de los que vemos una muestra en la imagen.

<center>

![Placas protoboard](../img/conceptos/discretos/proto.png)  
*Placas protoboard*

</center>

Hay dos cosas importantes en este tipo de componente, la primera es no introducir en los agujeritos componentes o cables de mas de 0.5mm de diámetro porque a la larga esto provocará falsos contactos con otros componentes y la segunda es tener muy claro como van conectados internamente los agujeros.

<center>

![Conexiones internas en placas protoboard](../img/conceptos/discretos/proto_conex.png)  
*Conexiones internas en placas protoboard*

</center>

## <FONT COLOR=#007575>**Resistencias**</font>
La resistencia es un componente electrónico del grupo denominado pasivos que está diseñado para oponerse al paso de la corriente. El valor de la resistencia se expresa en ohmios o sus múltiplos. Se fabrican principalmente de carbón (la mina de un lápiz es una resistencia) o de pelicula metálica y se comercializan en una amplia gama de valores. Su aspecto lo vemos en la imagen.

<center>

![Resistencias](../img/conceptos/discretos/res.png)  
*Resistencias*

</center>

Las resistencias están definidas por tres características fundamentales:

- el valor resistivo
- la potencia máxima que puede disipar
- la tolerancia

Hay resistencias con valores de Ohmios (Ω), Kilohmios (KΩ), Megaohmios (MΩ) y otros múltiplos y submúltiplos. La equivalencias entre ellas es:

* 1 Kilohmio (KΩ) = 1,000 Ohmios (Ω)
* 1 Megaohmio (MΩ) = 1,000,000 Ohmios (Ω) = 1,000 Kilohmios (KΩ)

Para poder saber que valor y tolerancia tiene una resistencia, existe un código de colores que nos ayuda a obtener con facilidad estos valores. La potencia no se indica expresamente en este tipo de resistencias y depende de su tamaño, por lo que con el uso nos iremos acostumbrando.

Existen resistencia de 3 (en desuso), 4, 5 y 6 bandas de colores y cada una se lee de manera diferente aunque parecida. Veamoslas.

Existen muchas páginas y aplicaciones que nos ayudan a averiguar el valor de una resistencia por sus bandas de color. Una muy completa y fácil de usar es la de [Digikey](https://www.digikey.es/es/resources/conversion-calculators/conversion-calculator-resistor-color-code), una tienda de componentes que además nos ofrece otras muchas calculadoras que nos resultarán útiles.

### <FONT COLOR=#AA0000>4 bandas</font>
En estas, una de las bandas estará más cercana al terminal o patilla, puede ser mas ancha y es esa su primera cifra significativa o banda 1, la siguiente es la banda 2, la siguiente es la banda multiplicadora y la cuarta banda es la banda de tolerancia, esta banda normalmente es mas estrecha. A continuación vemos como se leen estas resistencias.

<center>

![Resistencias de cuatro bandas](../img/conceptos/discretos/4bandas.png)  
*Resistencias de cuatro bandas*

</center>

El valor se obtendría poniendo: 56 x 10⁴ = 560k +/- 5%

### <FONT COLOR=#AA0000>5 bandas</font>
En este caso hay tres cifras significativas y se leen como vemos a continuación.

<center>

![Resistencias de cinco bandas](../img/conceptos/discretos/5bandas.png)  
*Resistencias de cinco bandas*

</center>

El valor se obtendría poniendo: 247 x 10² = 24700 = 24K7 +/- 5%

### <FONT COLOR=#AA0000>6 bandas</font>
A estas resistencias se añade una sexta banda como última banda para indicar el coeficiente de temperatura y también tienen tres cifras signiticativas. A continuación vemos como se leen. El coeficiente de temperatura indica cuanto cambia el valor de la resistencia en función de la temperatura utilizando normalmente ppm/K (partes por millón por grado Kelvin) como unidad. Es muy raro ver resistencias de seis bandas como componente habitual.

<center>

![Resistencias de seis bandas](../img/conceptos/discretos/6bandas.png)  
*Resistencias de seis bandas*

</center>

El valor se obtendría poniendo: 412 x 10³ = 412K +/- 1% y 5 ppm/K

## <FONT COLOR=#007575>**El diodo LED**</font>
El diodo LED (Light Emitting Diode) es un diodo semiconductor capaz de emitir luz, lo mas usuales dentro del espectro visible aunque también pueden ser de infrarrojos, laser, etc. Su uso mas habitual es como indicador y, últimamente cada vez mas frecuentes en iluminación. Sus principales ventajas frente a luces incandescentes son:

* Menor consumo de energía
* Mayor vida útil
* Menor tamaño
* Gran durabilidad y fiabilidad
* En la imagen siguiente vemos el aspecto físico que tiene y su símbolo electrónico.

<center>

![Aspecto y símbolo del LED](../img/conceptos/discretos/LED.png)  
*Aspecto y símbolo del LED*

</center>

El color de la cápsula es simplemente orientativo, es la longitud de onda quien define realmente el color de la luz emitida. Por ello el LED con la cápsula transparente puede emitir en cualquiera de los colores del espectro visible.

La forma de la capsula mas habitual es cilíndrica de 3 o 5 mm de diámetro, aunque existen otras formas menos usuales como las que vemos en la imagen siguiente:

<center>

![Tipos de encapsulados para LEDs](../img/conceptos/discretos/encapsulados.png)  
*Tipos de encapsulados para LEDs*

</center>

El LED es un dispositivo que tiene polaridad siendo su comportamiento el siguiente: En polarización directa (ánodo a positivo y cátodo a negativo) el LED emite luz y en polarización inversa (ánodo negativo y cátodo positivo) se comporta prácticamente como un interruptor abierto.

Para su correcto funcionamiento el diodo LED se polariza poniéndole en serie una resistencia que limita la corriente que pasa a través del mismo y, por tanto, determina el nivel de brillo de la luz emitida.

Sin entrar en detalles en la tabla siguiente se dan los valores de tensión directa (VF) y corriente directa (IF) para los colores mas habituales de LEDs. A partir de estos valores y el valor de tensión de alimentación de nuestro LED podemos calcular el valor de la resistencia serie sin mas que aplicar la formula indicada.

<center>

![Tensión y corriente para distintos colores](../img/conceptos/discretos/colores-calculo-R.png)  
*Tensión y corriente para distintos colores*

</center>

## <FONT COLOR=#007575>**Pulsador**</font>
Un botón pulsador o abreviadamente pulsador es un componente eléctrico que permite o impide el paso de la corriente eléctrica cuando se acciona. El pulsador solo permanece abierto o cerrado cuando lo presionamos y unicamente mientras lo mantenemos presionado. Al soltarlo vuelve a su posición inicial o de reposo.

En función de como están los contactos cuando el pulsador está en reposo, tenemos dos tipos diferentes: Normalmente Abierto y Normalmente Cerrado. Siendo el mas utilizado es pulsador normalmente abierto.

El funcionamiento del pulsador normalmente abierto es:

- Pulsador en reposo: el pulsador esta abierto y la corriente no puede pasar a través del mismo.
- Pulsador accionado: se conoce como posición de Trabajo y mientras se mantenga pulsado la corriente puede pasar por el pulsador.

En la tabla siguiente vemos la simbología y algunos ejemplos del aspecto físico de estos elementos del tipo que habitualmente se utiliza con este tipo de placas.

<center>

![Símbolos y aspecto real de un pulsador](../img/conceptos/discretos/aspecto-pulsadores.png)  
*Símbolos y aspecto real de un pulsador*

</center>

Existen muchos tipos y formas de pulsadores, pero los mas utilizados con este tipo de placas los vemos a continuación. Los de mayor tamaño suelen ir acompañados de una pieza de diferentes colores para colocar por presión en la parte amarilla (puede ser de otros colores) el pulsador y crear una tecla. Se aprecian las dimensiones así como la forma en que van conectados internamente los pines.

<center>

![Pulsadores mas usuales](../img/conceptos/discretos/pulsadores_usuales.png)  
*Pulsadores mas usuales*

</center>

Mediante la configuración adecuada podemos convertir un pulsador en un elemento de entrada a algún pin de nuestra placa de control. Las configuraciones más básicas posibles con pulsadores las podemos ver en la imagen siguiente.

<center>

![Configuración circuito elemental con pulsador](../img/conceptos/discretos/circuitos-pulsador.png)  
*Configuración circuito elemental con pulsador*

</center>

### <FONT COLOR=#AA0000>Rebotes</font>
Cuando accionamos un pulsador, este no cambia de un estado a otro inmediatamente. En el proceso de cambio de estado del pulsador se producen pequeñas vibraciones mecánicas que provocan una serie de efectos transitorios que pueden llegar a convertirse en un problema real. Supongamos que estamos contando pulsaciones, si cada vez que pulsamos esos efectos dan como resultado mas de un pulsación, es evidente que tenemos un problema. Estos efectos se estabilizan muy rapidamente porque duran muy poco tiempo y por tanto a nivel humano no son detectables, pero a nivel de microcontrolador si lo son. El fenomeno también ocurre al soltar el pulsador. Este fenómeno no deseado es lo que se conoce como "rebote".

<center>

![Fenomenos transitorios de rebotes en un pulsador](../img/conceptos/discretos/rebotes.png)  
*Fenomenos transitorios de rebotes en un pulsador*

</center>

Por lo tanto, es muy posible que, cuando detectamos el estado de un pulsador, obtengamos múltiples acciones de pulsación y liberación en un ciclo de pulsación. Este rebote puede llegar a confundir el funcionamiento del microcontrolador debido a la alta velocidad a la que trabaja. Por eso es conveniente eliminar el efecto de los rebotes en nuestros circuitos. Se puede hacer por hardware, colocando un condensador de 1uF, o incluso de mas capacidad, en paralelo con el pulsador. Tambien se pueden eliminar por software dejando transcurrir unos 150ms entre el momento que se acciona el pulsador y el momento en que la lectura se hace efectiva o bien comprobando el estado del botón varias veces y cuando ha transcurrido un tiempo considerar el estado del botón como estable. Dicho de otro modo, con una serie de lecturas y retardos del estado del pulsador se desechan esas pulsaciones no deseadas.

## <FONT COLOR=#007575>Interruptor</font>
La diferencia entre un pulsador y un interruptor radica en que el pulsador no mantiene su posición de trabajo si dejamos de accionarlo mientras que el interruptor si mantiene la posición, permaneciendo en la misma hasta que volvamos a accionarlo. Es decir, el interruptor cambia de posición cada vez que lo accionamos siendo totalmente estable cada posición. Hay ocasiones en que visualmente incluso pueden parecer iguales y solo se diferencian en su modo de funcionamiento.

Los interruptores se clasifican en función del tipo de conexión que realizan, como son el número de polos (Pole) y el de circuitos (Throw). Se define el número de polos como el número de circuitos capaz de controlar el interruptor. Puden ser unipolares, para un solo circuito o bipolares para controlar dos circuitos separados. Podemos decir que un interruptor bipolar son dos interruptores unipolares accionados por el mismo actuador. Por otro lado Throw se refiere al número de salidas que tiene cada polo. En base a esto tenemos:

<center>

|Tipo|Procedencia|Significado|Símbolo|
|:-:|---|---|:-:|
|SPST|Single Pole, Single Throw|Un polo, un circuito|![](../img/conceptos/discretos/SPST.png)|
|SPDT|Single Pole, Double Throw|Un polo, dos circuitos|![](../img/conceptos/discretos/SPDT.png)|
|DPST|Double Pole, Single Throw|Dos polos, un circuito|![](../img/conceptos/discretos/DPST.png)|
|DPDT|Double Pole, Double Throw|Dos polos, dos circuitos|![](../img/conceptos/discretos/DPDT.png)|

</center>

En la imagen siguiente quedará mas claro el tema de Pole y Throw.

<center>

![SPST, SPDT, DTSP y DPDT](../img/conceptos/discretos/P_T.png)  
*SPST, SPDT, DTSP y DPDT*

</center>

En el caso de los interruptores también pueden ser Normalmente Abiertos o Normalmente Cerrados y existen de muchos tipos en función de la aplicación que se les va a dar. También existen de mas de dos circuitos e incluso de varios polos.

Por su forma de accionamiento pueden ser: rotatorios, basculantes, deslizantes, tipo DIP, etc. En la imagen vemos el aspecto real de algunos de ellos.

<center>

![Diversos tipos de interruptores](../img/conceptos/discretos/interrup_imag.png)  
*Diversos tipos de interruptores*

</center>
