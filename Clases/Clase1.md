# Presentación 
## Ventajas python 
    - Fácil de aprender y leer.
    - Portable 
    - Popular 
    - Multiparadigma 
    - Aplicación en diversas áreas
    
    (Librerias)[https://python.libhunt.com/]
## Curva de aprendizaje  

!(curva)[https://www.test-oposiciones.es/wp-content/uploads/2018/03/Curva-aprendizaje-1024x752.png]


# Algortimos 
Es un conjunto de instrucciones o reglas definidas y no ambiguas, ordenadas y finitas que permite, típicamente, solucionar un problema, realizar un cómputo, procesar datos y llevar a cabo otras tareas o actividades.​ Dados un estado inicial y una entrada, siguiendo los pasos sucesivos se llega a un estado final y se obtiene una solución. 

Un algoritmo es univoco, lo que implica que si se ejecuta varias veces el mismo algoritmo sobre un conjunto de datos de entrada, siempre se obtiene la misma solución a la salida. Además, el resultado debe generarse en un tiempo finito.


## Algoritmos como funciones.
Se puede concebir como una función matemática que transforma los datos de un problema (entrada) en los datos de una solución (salida). 

Si un fenmóeno o problema de la realidad puede expresarse como una función matemática o lógica entonces puede existir un algoritmo que lo simule o lo resuelva. No todos los problemas tienen solución. 

### Escribir los algoritmos de los siguientes problemas:
- división de un número 
- promedio de calificaciones
- promedio de un circulo
- saber si una palabra es palíndromo 

# Lenguaje 
El lenguaje natural es la lengua o idioma hablado o escrito por humanos para propósitos generales de comunicación. Son aquellas lenguas que han sido generadas espontáneamente en un grupo de hablantes con propósito de comunicarse

# Lenguajes de programación 

Un lenguaje de programación se conforma de una serie de símbolos y reglas de sintaxis y semántica que definen la estructura principal del lenguaje y le dan un significado a sus elementos y expresiones.


La función principal de los lenguajes de programación es escribir programas que permiten la comunicación usuario-máquina.

- sintaxis 
    Reglas que gobiernan la combinatoria de los símbolos y la formación de unidades superiores a estos)
- semántica 
    Reglas que gobiernan los aspectos del significado, sentido o interpretación del significado de un determinado elemento, símbolo, palabra, expresión o representación formal)
# Clasificacion de los lenguajes de programación 

## Alto nivel 
Los lenguajes de programación de alto nivel se caracterizan porque su estructura semántica es muy similar a la forma como escriben los humanos, lo que permite codificar los algoritmos de manera más natural, en lugar de codificarlos en el lenguaje binario de las máquinas, o a nivel de lenguaje ensamblador.

## Bajo nivel 
Un lenguaje de programación de bajo nivel es el que proporciona poca o ninguna abstracción del microprocesador de una computadora. Consecuentemente, su trasladado al lenguaje máquina es fácil. El término ensamblador (del inglés assembler) se refiere a un tipo de programa informático encargado de traducir un archivo fuente, escrito en un lenguaje ensamblador, a un archivo objeto que contiene código máquina ejecutable directamente por la máquina para la que se ha generado.

## Lenguaje máquina 
Es el sistema de códigos interpretable directamente por un circuito microprogramable, como el microprocesador de una computadora. Este lenguaje se compone de un conjunto de instrucciones que determinan acciones que serán realizadas por la máquina. Y un programa de computadora consiste en una cadena de estas instrucciones de lenguaje de máquina (más los datos). Normalmente estas instrucciones son ejecutadas en secuencia, con eventuales cambios de flujo causados por el propio programa o eventos externos. El lenguaje máquina es específico de cada máquina o arquitectura de la máquina, aunque el conjunto de instrucciones disponibles pueda ser similar entre ellas.

# Lenguajes compilados vs lenguajes interpretados 
# Elementos de los lenguajes de programación 


## Variables 
Son elementos que permiten nombrar y almacenar información durante la ejecución de un programa. 

```
variable = <valor>
variable = 10
variable = 5.5
variable = 'palabra'
```

## Tipos y estructuras de datos

Las estructuras de datos son elementos de los lenguajes de programación que permiten manipular de forma más eficiente variables diversas: numéricas o tipo texto (cadenas de caracteres), y otras más complejas, como vectores, matrices y apuntadores, etcétera

```
lista = [0,1,2,3,4,5]
matrices = [[1,0,0],
            [0,1,0],
            [0,0,1],
            ]
diccionario = {"juan":9,"paco":8, "pedro":5, "delamar":10 }
```

## Instrucciones
Son estructuras gramaticales predefinidas, muy parecidas al lenguaje humano, para generar secuencias de acciones que conformen un programa. Van desde los operadores aritméticos y lógicos básicos (sumas, restas, and, or) hasta instrucciones más especializadas para realizar diversas acciones dentro del programa, como guardado de archivos, volcado de pantalla de un texto, etcétera

```
a = 5
b = 10 
c = a + b
print("resultado de la suma",str(c))
```


## Control de flujo
Se refiere a la secuencia de acciones de un programa. En ocasiones, dentro de la secuencia de instrucciones, hay puntos donde el programa debe tomar decisiones con base en el valor de una variable o el cumplimiento de una cierta condición. El tipo de instrucciones que posibilitan dichas acciones son, precisamente, las de control de flujo: condicionales (if-then-else), de bucle (for o while) o selección (case).

```
if a > b : 
    print("a es el maximo")
else:
    print("b es el minimo)

for i in lista :
    print(i)

while i < 10:
    print(i)
    i = i + 1

```


## Funciones y objetos 
una serie de instrucciones localizadas fuera del cuerpo principal del programa que realizan una tarea específica y regresan un resultado; pueden ser empleadas a lo largo de un programa una o varias veces. Los lenguajes de alto nivel, además de las funciones predefinidas por el propio lenguaje, permiten al programador diseñar y construir sus propias funciones.

```
def suma(a,b):
    resultado = a + b
    return resultado

a = 5
b = -2 
c = suma(a,b)
print("resultado de la suma", str(c))
```


https://programas.cuaed.unam.mx/repositorio/moodle/pluginfile.php/1023/mod_resource/content/1/contenido/index.html

https://www.learnpython.org/es/

