# ejercicio 1 
print("Hola Mundo!")

# ejercicio 2
nombre = input("Por favor, ingrese su nombre: ")
print(f"Hola {nombre}!")

# ejercicio 3
nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = input("Por favor, ingrese su edad: ")
lugar_de_residencia = input("Por favor, ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}.")

# ejercicio 4
import math
radio_circulo = float(input("Por favor, ingrese el radio del círculo: "))
area_circulo = math.pi * (radio_circulo)**2
perimetro_circulo = 2 * math.pi * radio_circulo
print(f"El área del círculo es {area_circulo} y el perímetro de {perimetro_circulo}.")

# ejercicio 5
cantidad_segundos = float(input("Por favor, ingrese la cantidad de segundos a convertir: "))
cantidad_horas = round(cantidad_segundos / 3600, 2)
print(f"El equivalente a {cantidad_segundos} segundos son {cantidad_horas} horas.")

# ejercicio 6
n_multiplicar = int(input("Por favor, ingrese un número entero: "))
print(f"""
  {n_multiplicar} x 0 = {n_multiplicar * 0}
  {n_multiplicar} x 1 = {n_multiplicar * 1}
  {n_multiplicar} x 2 = {n_multiplicar * 2}
  {n_multiplicar} x 3 = {n_multiplicar * 3}
  {n_multiplicar} x 4 = {n_multiplicar * 4}
  {n_multiplicar} x 5 = {n_multiplicar * 5}
  {n_multiplicar} x 6 = {n_multiplicar * 6}
  {n_multiplicar} x 7 = {n_multiplicar * 7}
  {n_multiplicar} x 8 = {n_multiplicar * 8}
  {n_multiplicar} x 9 = {n_multiplicar * 9} """)

# ejercicio 7
numero_a = float(input("Por favor, ingrese un número distinto de 0: "))
numero_b = float(input("Por favor, ingrese otro número distinto de 0: "))
suma_a_b = numero_a + numero_b
division_a_b = round(numero_a / numero_b, 2)
multiplicacion_a_b = numero_a * numero_b
resta_a_b = numero_a - numero_b
print(f""" Resultado de la suma: {suma_a_b} Resultado de la división: {division_a_b}
  Resultado de la multiplicación: {multiplicacion_a_b}
  Resultado de la resta: {resta_a_b} """)

# ejercicio 8
peso = float(input("Por favor, ingrese su peso: "))
altura = float(input("Por favor, ingrese su altura: "))
imc = round(peso / altura**2, 2)
print(f"Su IMC es de: {imc}.")

# ejercicio 9
temperatura_celsius = float(input("temperatura en °C: "))
temperatura_fahrenheit = round((9/5)*temperatura_celsius+32, 2)
print(f"{temperatura_celsius} °C equivalen a {temperatura_fahrenheit} °F.")

# ejrcicio 10
numero_a = float(input("ingrese el primer número: "))
numero_b = float(input("ingrese el segundo número: "))
numero_c = float(input("ingrese el tercer número: "))
suma_a_b_c = numero_a + numero_b + numero_c
promedio_a_b_c = round(suma_a_b_c/3, 2)
print(f"El promedio de los números ingresados es {promedio_a_b_c}.")