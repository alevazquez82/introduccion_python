
print("hola mundo")
#comentario de una linea
"""
comentario
de
varias
lineas
"""
#Numeros enteros
edad = 25
cantidad = 100
#Numeros flotantes
precio = 9.99
altura = 1.75
#Cadenas de texto
nombre = "Alejandro"
mensaje = "Hola Python"
#Booleanos
es_mayor_de_edad = True
tiene_descuento = False
#Operadores aritmeticos
a = 10
b = 3
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
division_entera = a//b
modulo = a % b
exponenciacion = a ** b
#De comparacion
c = 10
d = 3
igual = c == d
diferente = c != d
mayor_que = c > d
menor_que = c < d
mayor_o_igual = c >= d
menor_o_igual = c <= d
#Logicos
e = 10
f = 3
resultado_and = (e > 5) and (f < 5)#True
resultado_or = (e > 15) or (f < 5)#True
resultado_not = not (e > 5) #False
#Estructuras de control
#IF
edad = 18
if edad >= 18:
	print ("Sos mayor.")
#IF-ELSE
edad = 15
if edad >= 18:
	print("Sos mayor.")
else:
	print("Sos menor")
#IF-ELIF-ELSE
"""
if condicion1:
	Bloque de codigo a ejecutar si la condicion1 es verdadera 
	instruciones
elif condicion2:
	Bloque de codigo a ejecutar si la condicion2 es verdadera 
	instruciones
"""
calificacion = 40
if calificacion >= 90:
	print("Excelente")
elif calificacion >= 80:
	print("Muy bueno")
elif calificacion >= 70:
	print("Bueno")
else:
	print("Necesita mejorar")
#Bucles/loops
#For
"""
for variable in secuencia:
	Bloque de codigo a repetir
	instrucciones
"""
#Ejemplo
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
	print(fruta)
#While	
"""
while condicion:
	Bloque de codigo a repetir
	instrucciones
"""
#Ejemplo
contador = 0
while contador < 5:
	print(contador)
	contador +=1
#Control de bucles
#Break
contador = 0
while True:
	print(contador)
	contador += 1
	if contador == 5:
		break
#Continue
for i in range(10):
	if i % 2 == 0:
		continue
	print(i)
#Pass(La instruccion pas es una operacion que no hace nada, Puede ser util para reservar un bloque para implementarlo mas adelante)
for i in range(5):
	pass
#Estructuras de datos
#Listas
frutas = ["manzana", "banana", "naranja"]
print(frutas[0])
print(frutas[1])
print(frutas[2])
#Metodos de listas
"""
append(elemento): agrega un elemento al final de la lista}
insert(indice, elemento): inserta un elemento en una posicion especifica de la lista
remove(elemento): elimina la primera aparicion de un elemento en la lista
pop(indice): elimina y devuelve el elemento en una posicion especifica de la lista
sort(): ordena los elementos de lalista en orden ascendente
reverse(): invierte el orden de los elementos en la lista
"""
frutas = ["manzana", "banana", "naranja"]
frutas.append("pera")
print(frutas)
frutas.insert(1, "uva")
print(frutas)
frutas.remove("banana")
print(frutas)
fruta_eliminada = frutas.pop(2)
print(frutas)
print(fruta_eliminada)
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)
#Listas de comprension: permiten filtras y transformar los elementos de una lista en una sola linea de codigo
#nueva_lista = [expresion for elemento in secuencia if condicion] 
numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)
#Tuplas: a diferencia de las listas las tuplas son inmutables.lo que significa que no se pueden modificar una vez creadas.
"""
punto = (3, 4)
print(punto[0])
print(punto[1])
Metodos de tuplas
count(elemento):devuelve el numero de veces que aparece un elemento en la tupla
index(elemento): devuelve el indice de la primera aparicion de un elemento en la tupla.Opcionalmente, se puede especificar el inicio y fin de la busqueda
len(tupla): aunque no es un metodo de la tupla propiamente dicho, esta funcion devuelve la longitud de la tupla
"""
mi_tupla = (1, 2, 3, 2, 4, 2)
print (mi_tupla.index(2))
print(mi_tupla.index(2, 2))
print(mi_tupla.index(2, 2, 4))
#Diccionarios 
persona = {"nombre": "Alejandro", "edad": 25, "ciudad": "Madrid"}
print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])
#Metodos de diccionarios
"""
keys(): devuelve una ista de todas las claves del diccionario
values(): devuelve una vista de todos los valores del diccionario
items(): devuelve una vista de todos los pares clave-valor del diccionario
update(otro_diccionario): actualiza el diccionario con los pares clave-valor de otro diccionario
"""
print(persona.keys())
print(persona.values())
print(persona.items())
persona.update({"profecion": "desarrollador"})
print(persona)
#Conjuntos(set)
"""
son una estructuta de datos mutable y no ordenada que permite almacenar
una coleccion de elementos unicos.Los conjuntos se encierran entre llaves{}
o se crean utilizando la funcion set()
frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3, 4, 5])
Los conjuntos admiten operaciones matematicas de conjuntos, como la union(|),
la interseccion(&), la diferencia(-) y la diferencia simetrica(^)
"""
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1 | conjunto2
print(union)
interseccion = conjunto1 & conjunto2
print(interseccion)
diferencia = conjunto1 - conjunto2
print(diferencia)
diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)
"""
metodos
add(elemento): agrega un elemento al conjunto
remove(elemento): elimina un elemento del conjunto. Si el elemento no existe genera un error
discard(elemento): elimina un elemento del conjunto si esta presente. Si el elemento no existe, no hace nada
clear(): elimina todos los elementos del conjunto
"""
#Ejemplo
frutas = {"manzana", "banana", "naranja"}
frutas.add("pera")
print(frutas)
frutas.remove("banana")
print(frutas)
frutas.discard("uva")
print(frutas)
frutas.clear()
print(frutas)

numero = 7
if numero % 2 == 0:
	resultado = "Par"
else:
	resultado = "impar"
print(resultado)

def multiplicar (a, b):
	return a * b
resultado = multiplicar(5,3) + multiplicar(2, 4)

