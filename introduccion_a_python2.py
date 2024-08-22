#Definicion y llamada de funciones
"""
def saludo():
	print("!Hola, mundo¡")
saludo()
"""
#Parametros y argumentos
"""
def  saludo(nombre):
	print(f"!Hola, {nombre}!")
saludo("Alejandro")
"""
#Valores de retorno
"""
def suma(a, b):
	return a + b
resultado = suma(3, 4)
print(resultado)
"""
#Funciones anonimas(lambda)
"""
cuadrado = lambda x : x ** 2
print(cuadrado(5)) 
"""
#Alcance de las variables(local vs global)
"""
def funcion():
	variable_local = 10
	print(variable_local)

variable_global = 20
def funcion2(): 
	print(variable_global)

funcion()
funcion2()
print(variable_global)
print(variable_local)#genera error por no estar definida en este alcance
"""
#Funciones definidas por el usuario
"""
def calcular_media(*numeros):
	suma = sum(numeros)
	cantidad = len(numeros)
	media = suma / cantidad
	return media
print("Media: ", calcular_media(10, 20, 30, 40))

def sumar_3(x):
	return x + 3
sumar = lambda x: x + 3
print("Sumarle 3 a un numero: ", sumar(5))
"""
#Documentacion de funciones(docstring)
#def area_rectangulo(base, altura):
"""
	calcula el area de un rectangulo
	Args:
		base(float): La base del rectangulo
		altura(float): La altura del rectangulo
	returns:
		float: El area del rectangulo.
"""
#return base * altura
#Funciones con numero variable de argumentos
"""
def suma_variable(*numeros):
	total = 0
	for numero in numeros:
		total += numero
	return total
print(suma_variable(1, 2, 3))
print(suma_variable(4, 5, 6, 7))
"""
#Try
"""
try:
	#Codigo que puede generar una excepcion
	resultado = 10 / 0 
	print(resultado)
except ZeroDivisionError:
	print("Error: Division por cero")
"""
#Except
"""
try:
	#Codigo que puede generar una exccepcion
	resultado = 10 / 0
	print(resultado)
except ZeroDivisionError:
	print("Error: Division por cero") 
except ValueError:
	print("Error: Valor invalido")
"""
#Finally
"""
try:
	#Codigo que puede generar una excepcion
	archivo = open("archivo.txt", "r")
	#Realizar opeciones con el archivo
except FileNotFoundError:
	print("Error: Archivo no encontrado")
finally:
	archivo.close()#Cerrar el archivo siempre, incluso si ocurra una excepcion
"""
#Excepciones personalizadas
"""
def funcion():
	#Codigo que puede generar una excepcion personalizada
	if condicion:
		raise Exception("Descripcion del error")
try:
	funcion()
except Exception as e:
	print(f"Error: {str(e)}")
"""
#Entradas/salidas
#Entrada de datos del usuario
"""
nombre = input("Ingresar nombre: ")
edad = input("ingresar tu edad: ")
print("Hola " + nombre + "!")
print("Tu edad es: " + edad + "años.")

edad = int(input("Ingresa tu edad:"))
if edad >= 18:
	print("sos mayor")
else:
	print("sos menor")

nombre = "Juan"
edad = 25
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")
"""
#Lectura t escritura de archivos
#Lectura de archivos
"""
archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

#Escritura de archivos
archivo = open("datos.txt", "w")
archivo.write("Hola, mundo")
acrivo.close

with open("datos.txt", "r") as archivo:
	contenido = archivo.read()
	print(contenido)
"""
#Importacion y creacion de modulos
#importar modulos
"""
import math
resultado = math.sqrt(25)
print(resultado)
from math impor sqrt
resultado = sqrt(25)
print(resultado)
"""
#Funciones y clases de modulos estadar
"""
import random
import datetime
numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)
fecha_actual = datetime.datetime.now()
print(fecha_actual)
"""
#Creacion de modulos propios
#Crear y utilizar modulos personalizados
#mi_modulo.py
"""
def saludar(nombre):
	print(f"hola, {nombre}!")
def calcular_suma(a, b):
	return a + b
import mi_modulo
mi_modulo.saludar("Juan")
resultado = mi_modulo.calcular_suma(5, 3)
print(resultado)
# operaciones.py
def sumar(a, b):
	return a + b

def restar(a, b):
	return a - b

# utilidades.py
def imprimir_mensaje(mensaje):
	print(mensaje)
def obtener_nombre_usuario():
	return input("ingresa tu nombre: ")
import operaciones
import utilidades
resultado = operaciones.sumar(5, 3)
utilidades.imprimir_mensaje(f"el resultado de la suma es: {resultado}")

nombre = utilidades.obtener_nombre_usuario()
utilidades.imprimir_mensaje(f"hola, {nombre}!")
"""
#Paquetes
"""
mi_paquete/
	__init__.py
	modulo1.py
	modulo2.py
from mi_paquete import modulo1, modulo2

modulo1.funcion1()
modulo2.funcion2
"""