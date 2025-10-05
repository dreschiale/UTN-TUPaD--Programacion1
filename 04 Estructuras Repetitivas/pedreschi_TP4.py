#ejercicio 1
for i in range(101):
    print(i)
#ejercicio 2
num = int(input("Ingrese un número entero: "))
print(len(str(abs(num))))
#ejercicio 3
a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))
suma = sum(range(a + 1, b))
print(f"La suma de los números entre {a} y {b} es: {suma}")
#ejercicio 4
total = 0
while True:
    num = int(input("Ingrese un número entero (0 para terminar): "))
    if num == 0:
        break
    total += num
print(f"El total acumulado es: {total}")
#ejercicio 5
import random
num_aleatorio = random.randint(0, 9)
intentos = 0
while True:
    num = int(input("Adivine el número (0-9): "))
    intentos += 1
    if num == num_aleatorio:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
    else:
        print("Intenta de nuevo.")
#ejercicio 6
for i in range(100, -1, -2):
    print(i)
#ejercicio 7
num = int(input("Ingrese un número entero positivo: "))
suma = sum(range(num + 1))
print(f"La suma de los números entre 0 y {num} es: {suma}")
#ejercicio 8
pares = impares = negativos = positivos = 0
n = int(input("Ingrese la cantidad de números a procesar: "))
for i in range(n):
    num = int(input(f"Ingrese el número {i + 1}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Negativos: {negativos}")
print(f"Positivos: {positivos}")
#ejercicio 9
n = int(input("Ingrese la cantidad de números a procesar: "))
suma = 0
for i in range(n):
    num = int(input(f"Ingrese el número {i + 1}: "))
    suma += num
media = suma / n
print(f"La media de los números es: {media}")
#ejercicio 10
num = input("Ingrese un número: ")
print(num[::-1])