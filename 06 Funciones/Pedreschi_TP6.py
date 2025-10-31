#Actividad 1
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

#Actividad 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"
nombre = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre)
print(saludo)

#Actividad 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#Actividad 4
import math
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio
radio = float(input("Ingrese el radio del circulo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"Área del círculo: {area:.2f}")
print(f"Perímetro del círculo: {perimetro:.2f}")

#Actividad 5
def segundos_a_horas(segundos):
    return segundos / 3600
segundos = float(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos son equivalentes a {horas:.2f} horas.")

#Actividad 6
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
numero = int(input("Ingrese un numero: "))
tabla_multiplicar(numero)

#Actividad 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"
    return suma, resta, multiplicacion, division
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print("Resultados de las operaciones básicas:")
print(f"Suma: {a} + {b} = {suma}")
print(f"Resta: {a} - {b} = {resta}")
print(f"Multiplicación: {a} * {b} = {multiplicacion}")
print(f"División: {a} / {b} = {division}")

#Actividad 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.2f}")

#Actividad 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C es equivalente a {fahrenheit:.2f}°F")

#actividad 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
promedio = calcular_promedio(a, b, c)
print(f"El promedio es: {promedio:.2f}")