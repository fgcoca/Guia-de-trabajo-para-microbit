# <FONT COLOR=#8B008B>Data logging o registro de datos</font>
Un Data Logger es un registrador (grabador) de datos que trabaja en tiempo real de forma independiente. Cuando lo que necesitamos es registrar datos de forma prolongada hay que optar por sistemas de adquisición de datos DAQ o DAS.

Son muchas las características que definen a un Data Logger y son muchos y variados los tipos existentes. Nosotros no vamos a profundizar en nada de esto porque nuestro objetivo no es utilizar Data Loggers comerciales, sino utilizar la placa micro:bit para que se convierta en uno que nos sirva para nuestros experimentos. Dicho lo anterior veamos de forma somera algunas de estas características:

* Frecuencia. Es la velocidad a la que se muestrean los datos.
* Tipos de entradas de datos. Normalmente son de baja tensión DC, pequeñas corrientes (mA), temperatura humedad y señales pulsantes.
* Número de canales. Pueden ir desde 1 hasta mas de 1000 en registradores físicos. Cuando superan los 100 canales se suelen conectar Ethernet.
* Capacidad de almacenamiento. Se trata de la cantidad de datos que pueden almacenar en su memoria interna. Sus valores suelen ser altos debido sobre todo a lo poco que ocupan las tasas de muestreo. Veamos un ejemplo: grabamos 4 canales a una muestra (sample) de un byte cada segundo, lo que implica que $4\cdot1=4\space muestras\space por\space segundo\space(4\space S/s)$ que en una hora serían $4S\cdot 3600s = 14400\space S/h$

En el caso de la micro:bit V2 disponemos de sensores de luz, temperatura, magnetismo, aceleración y sonido que son susceptibles de almacenar para mas tarde recuperarlos y estudiarlos. Los datos permanecerán en la memoria de la micro:bit incluso sin estar alimentada. Los datos se podrán examinar a partir de tablas o con visualización previa de forma gráfica directamente desde la micro:bit ya que los datos los podemos descargar y ponerlos en una hoja de cálculo, con todo lo que esto conlleva.

Siempre que vamos a crear un registro de datos es una buena idea planificarlo:

* dedicir que datos vamos a recopilar
* con que frecuencia
* si vamos a añadir alguna indicación de que se están recopilando datos
* controlar el comienzo y el final del registro.
* decidir que debe pasar si la capacidad del registro se llena.
* cuando borrar los datos de la micro:bit, bien desde el propio programa o bien actualizando el firmaware de la misma.
