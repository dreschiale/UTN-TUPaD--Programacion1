#Actividad 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def mostrar_factoriales():
    num = int(input("Ingrese un número entero positivo: "))
    for i in range(1, num + 1):
        print(f"El factorial de {i} es {factorial(i)}")

mostrar_factoriales()

#Actividad 2
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def mostrar_serie_fibonacci():
    num = int(input("Ingrese la posición de la serie de Fibonacci que desea ver: "))
    for i in range(num + 1):
        print(f"F({i}) = {fibonacci(i)}")

mostrar_serie_fibonacci()

#Actividad 3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente < 0:
        return 1 / potencia(base, -exponente)
    else:
        return base * potencia(base, exponente -1)

def calcular_potencia():
    base = float(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    resultado = potencia(base, exponente)
    print(f"{base} elevado {exponente} igual a {resultado}")

calcular_potencia()

#Actividad 4
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

def convertir_decimal_a_binario():
    num = int(input("Ingrese un número entero positivo: "))
    if num < 0:
        print("Por favor, ingrese un número entero positivo.")
    else:
        print(f"La representación binaria de {num} es {decimal_a_binario(num)}")

convertir_decimal_a_binario()

#Actividad 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    else:
        return palabra[0].lower() == palabra[-1].lower() and es_palindromo(palabra[1:-1])

def verificar_palindromo():
    palabra = input("Ingrese una palabra para verificar si es un palíndromo: ")
    palabra = palabra.replace(" ", "").lower()
    if es_palindromo(palabra):
        print(f"{palabra} es un palíndromo.")
    else:
        print(f"{palabra} no es un palíndromo.")

verificar_palindromo()

#Actividad 6
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

def solicitar_numero():
    while True:
        try:
            num = int(input("Ingrese un número entero positivo: "))
            if num >= 0:
                return num
            else:
                print("Por favor, ingrese un número entero positivo.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")


num = solicitar_numero()
resultado = suma_digitos(num)
print(f"La suma de los dígitos de {num} es {resultado}.")

#Actividad 7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

num2 = solicitar_numero()
resultado = contar_bloques(num2)
print(f"El total de bloques necesarios es {resultado}.")

#Actividad 8
def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

def solicitar_digito():
    while True:
        try:
            dig = int(input("Ingrese un dígito (entre 0 y 9): "))
            if 0 <= dig <= 9:
                return dig
            else:
                print("Por favor, ingrese un dígito entre 0 y 9.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")


num3 = solicitar_numero()
digito = solicitar_digito()
resultado = contar_digito(num3, digito)
print(f"El dígito {digito} aparece {resultado} veces en el número {num3}.")

