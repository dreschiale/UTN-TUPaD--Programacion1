#Ejercicio 1
notas = [8, 9, 7, 6, 5, 4, 3, 2, 1, 10]
print("Notas:")
for nota in notas:
    print(nota)
promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.2f}")
nota_max = max(notas)
nota_min = min(notas)
print(f"Nota más alta: {nota_max}")
print(f"Nota más baja: {nota_min}")

#Ejercicio 2
productos = []
for i in range(5):
    producto = input(f"Ingrese producto {i+1}: ")
    productos.append(producto)
productos_ordenados = sorted(productos)
print("Productos ordenados:")
for producto in productos_ordenados:
    print(producto)
producto_eliminar = input("Ingrese el producto que desea eliminar: ")
if producto_eliminar in productos:
    productos.remove(producto_eliminar)
    print("Producto eliminado")
else:
    print("Producto no encontrado")
print("Productos:")
for producto in productos:
    print(producto)
#Ejercicio 3
import random
numeros = [random.randint(1, 100) for _ in range(15)]
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]
print("Números:")
for num in numeros:
    print(num)
print(f"Pares: {len(pares)}")
print(f"Impares: {len(impares)}")

#Ejercicio 4
valores = [1, 2, 2, 3, 4, 4, 5, 6, 6]
valores_unicos = list(set(valores))
print("Valores únicos:")
for valor in valores_unicos:
    print(valor)

#Ejercicio 5
estudiantes = ["Juan", "María", "Pedro", "Ana", "Luis", "Sofía", "Mateo", "Isabella"]
accion = input("¿Desea agregar o eliminar un estudiante? ")
if accion.lower() == "agregar":
    nombre = input("Ingrese el nombre del estudiante: ")
    estudiantes.append(nombre)
elif accion.lower() == "eliminar":
    nombre = input("Ingrese el nombre del estudiante: ")
    if nombre in estudiantes:
        estudiantes.remove(nombre)
    else:
        print("Estudiante no encontrado")
print("Estudiantes:")
for estudiante in estudiantes:
    print(estudiante)
#Ejercicio 6
numeros = [1, 2, 3, 4, 5, 6, 7]
numeros_rotados = [numeros[-1]] + numeros[:-1]
print("Números rotados:")
for num in numeros_rotados:
    print(num)

#Ejercicio 7
temperaturas = [
    [10, 20],
    [12, 22],
    [15, 25],
    [18, 28],
    [20, 30],
    [22, 32],
    [25, 35]]
promedio_minimas = sum(temp[0] for temp in temperaturas) / len(temperaturas)
promedio_maximas = sum(temp[1] for temp in temperaturas) / len(temperaturas)
amplitud_max = 0
dia_amplitud_max = 0
for i, temp in enumerate(temperaturas):
    amplitud = temp[1] - temp[0]
    if amplitud > amplitud_max:
        amplitud_max = amplitud
        dia_amplitud_max = i + 1
print(f"Promedio de mínimas: {promedio_minimas:.2f}")
print(f"Promedio de máximas: {promedio_maximas:.2f}")
print(f"Día con mayor amplitud térmica: {dia_amplitud_max}")

#Ejercicio 8
notas = [
    [8, 9, 7],
    [6, 5, 4],
    [3, 2, 1],
    [10, 9, 8],
    [7, 6, 5]]
for i, estudiante in enumerate(notas):
    promedio = sum(estudiante) / len(estudiante)
    print(f"Promedio del estudiante {i+1}: {promedio:.2f}")
for j in range(len(notas[0])):
    suma = sum(estudiante[j] for estudiante in notas)
    promedio = suma / len(notas)
    print(f"Promedio de la materia {j+1}: {promedio:.2f}")

#Ejercicio 9
tablero = [["-" for _ in range(3)] for _ in range(3)]
jugador = "X"

while True:
    # Imprimir tablero
    for fila in tablero:
        print(" | ".join(fila))
        print("---------")

    # Pedir coordenadas al jugador
    while True:
        try:
            fila = int(input(f"Jugador {jugador}, ingrese la fila (1-3): "))
            columna = int(input(f"Jugador {jugador}, ingrese la columna (1-3): "))
            if fila < 1 or fila > 3 or columna < 1 or columna > 3:
                print("Fila o columna inválida. Por favor, ingrese un número entre 1 y 3.")
            elif tablero[fila-1][columna-1] != "-":
                print("Casilla ocupada, intente de nuevo")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

    # Marcar la casilla
    tablero[fila-1][columna-1] = jugador

    # Verificar victoria
    victoria = False
    # Verificar filas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:
            victoria = True
    # Verificar columnas
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:
            victoria = True
    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador or \
       tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        victoria = True

    if victoria:
        # Imprimir tablero final
        for fila in tablero:
            print(" | ".join(fila))
            print("---------")
        print(f"Jugador {jugador} gana!")
        break

    # Verificar empate
    empate = True
    for fila in tablero:
        for casilla in fila:
            if casilla == "-":
                empate = False
                break
        if not empate:
            break

    if empate:
        # Imprimir tablero final
        for fila in tablero:
            print(" | ".join(fila))
            print("---------")
        print("Empate!")
        break

    # Cambiar jugador
    if jugador == "X":
        jugador = "O"
    else:
        jugador= "X"
#Ejercicio 10
ventas = [
    [10, 20, 30, 40, 50, 60, 70],
    [15, 25, 35, 45, 55, 65, 75],
    [20, 30, 40, 50, 60, 70, 80],
    [25, 35, 45, 55, 65, 75, 85]]

for i, producto in enumerate(ventas):
    total = sum(producto)
    print(f"Total vendido del producto {i+1}: {total}")

ventas_diarias = [sum(dia) for dia in zip(*ventas)] #zip cambierte filas en coumnas
dia_max_ventas = ventas_diarias.index(max(ventas_diarias)) + 1
print(f"Día con mayores ventas totales: {dia_max_ventas}")

producto_max_ventas = ventas.index(max(ventas, key=sum)) + 1
print(f"Producto más vendido en la semana: {producto_max_ventas}")
