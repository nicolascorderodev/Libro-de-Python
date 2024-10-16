#SINTAXIS: como usar el lenguaje creando las primeras variables y estrucutras de control.

#sintaxis hace referencia al conjunto de reglas que definen como se tiene que escribir el código en un determinado lenguaje de programación, es decir, hace referencia a la forma en la que debemos escribir las instrucciones para que el ordenador o más bien el lenguaje de programación nos entienda.
#En la mayoria de lenguajes existe una sintaxis común, como por ejemplo el uso de = para asignar un dato a una variable, o el uso de {} para designar bloques de código, pero Python tiene ciertas particularidades.
#La sintaxis es a la programación lo que la gramática es a los idiomas. De la misma forma que la frase "Yo estamos aqui" no es correcta, el siguiente código en Python no seria correcto, ya que no respeta las normas del lenguaje
'''
if($variable){
    x=9;
}
'''
#Python no soporta el uso de $ ni hace falta terminar las lineas con ; como en otros lenguajes, y tampoco hay que usar {} en estrucutras de control como en el if.
#"Un idioma no se habla con simplemente saber todas sus palabras, en la programación pasa igual, no basta con saber la sintaxis de un lenguaje para programar correctamente en el, podemos empezar a programar pero el uso de un lenguaje de programación va mucho más alla de la sintaxis."

#Defino una variable x con una cadena
x = "El valor de (a+b)*c es"

#Se pueden realizar multiples asignaciones
a, b, c = 4, 3, 2

#Realizo unas operaciones con a,b,c
d = (a+b)*c

#Defino una variable booleana
imprimir = True

#Si imprimir, print()
if imprimir:
    print(x, d)
#Se observa que la sintaxis de Python es muy parecida al lenguaje natural o pseudocódigo, lo que hace que sea relativamente facil de leer. Otra ventaja es que no se necesita nada más como en otros lenguajes como C o Java que toca crear la función main().


#COMENTARIOS

#Ofrecen información relevante acerca del código sin afectarlo(comentario de una linea)

'''
#Comentario de varias lineas
A diferencia del anterior con este podemos comentar varias lineas de codigo sin necesidad de usar el # en cada una.
'''


#INDENTACIÓN Y BLOQUES DE CÓDIGO

#Los bloques de código se representan con indentación y aunque hay un poco de debate con respecto a usar tabulador o espacios, la normal general es usar 4 espacios.

#En el siguiente codigo tenemos un condicional if. Justo después tenemos un print() indentado con cuatro espacios. Por lo tanto todo lo que tenga esa indentación pertenecerá al bloque del if.

if True:
    print("True")

#Esto es muy importante ya que el código anterior y el siguiente no son lo mismo. De hecho el siguiente codigo daría un error ya que el if no contiene ningún bloque de código, y eso es algo que no se puede hacer en Python.
'''
if True:
print("True")
'''

#Por otro lado, a diferencia de otros lenguajes de programación, no es necesario utilizar ; para terminar cada línea.
'''
Otros lenguajes como C requiere de ; al final de cada línea
x = 10;
'''


#MULTIPLES LÍNEAS

#Se puede dar el caso de que queremos tener una sola instrucción en varias lineas de código. Uno de los motivos principales es que sea DEMASIADO LARGA y de hecho en la especficación PEP8 se recomienda que las lineas no excedan los 79 caracteres, haciendo uso del \ se puede romper el código en varias lineas, lo que hace que sea mas legible.
x = 1 + 2 + 3 + 4 + \
5 + 6 + 7 + 8

#Si por el contrario estamos dentro de un bloque rodeado con paréntesis bastaria con saltar a la siguiente línea.
x = (1 + 2 + 3 + 4 +
    5 + 6 + 7 + 8)

#Se puede hacer lo mismo para llamadas a funciones
def funcion(a, b, c):
    return a+b+c
d = funcion(10,
            10,
            10)
print(d)


#CREANDO VARIABLES

#En documentos anteriores se vio como crear una variable y asignarle un valor usando =. Existen también otras formas de hacerlo de una manera un poco más sofisticada.

#Asignar el mismo valor a diferentes variables
x = y = z = 10

#Asignar valores separados por coma.
x, y = 4, 2
x, y, z = 1, 2, 3


#NOMBRANDO VARIABLES

#Se le puede dar a la variables como uno quiera, pero es importante saber que las mayúsculas y minúsculas son importantes. Las variables x y X son distintas.

#Por otro lado existen ciertas normas a la hora de nombrar variables:

'''
-El nombre no puede empezar por un número.

-No se permite el uso de guiones.

-Tampoco se permite el usso de espacios.
'''

#Ejemplos de variables válidas y no válidas.

#Válido
_variable = 10
vari_able = 20
variable10 = 30
variable = 60
variaBle = 10

#No válido
#2variable = 10
#var-iable = 10
#var iable = 10

#Una última condición para nombrar a una variable en Python, es no usar nombres reservados para Python. Las palabras reservadas son utilizadas por Python internamente, por lo que no podemos usarlas para nuestras variables o funciones.

#PALABRAS RESERVADAS
# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']
#import keyword //Ver palabras reservadas
#print(keyword.kwlist) // Ver palabras reservadas
#PALABRAS RESERVADAS


#USO DE PARÉNTESIS

#Python soprta todos los operadores matemáticos más comunes, conocidos como operados aritméticos. Por lo tanto podemos realizar sumas, restas, multiplicaciones, exponentes(usando **)

#En este ejemplo se realizan varias operaciones en la misma línea, y almacenamos su resultado en y.
x = 10
y = x*3-3**10-2+3

#Pero el comportamiento del código anterior y el siguiente es distinto, ya que el uso de paréntesis () da prioridad a unas operaciones sobre otras.
x = 10
y = (x*3-3)**(10-2)+3


#VARIABLES Y ALCANCE

#Un concepto muy importante al definir una variable, es saber el alcance o scope que tiene. En el siguiente ejemplo la variable con valor 10 tiene un alcance global y la que tiene el valor 5 dentro de la función, tiene un alcance local. Esto significa que cuando hacemos print(x), estamos accediendo a la variable global x y no a la x definida dentro de la función.
x = 10

def funcion():
    x = 5

funcion()
print(x)