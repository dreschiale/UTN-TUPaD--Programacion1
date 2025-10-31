#Actividad 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)
#Actividad 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)
#Actividad 3
frutas = list(precios_frutas.keys())
print(frutas)
#Actividad 4
agenda = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    agenda[nombre] = numero
while True:
    nombre = input("Ingrese el nombre del contacto que desea consultar (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    if nombre in agenda:
        print(f"El número de teléfono de {nombre} es: {agenda[nombre]}")
    else:
        print(f"No se encontró un contacto con el nombre {nombre}")
#Actividad 5
frase = input("Ingrese una frase: ")
# Convertir a minúsculas y dividirla en palabras
palabras = frase.lower().split()
palabras_unicas = set(palabras)
frecuencia_palabras = {}
for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1
print(f"Palabras únicas: {palabras_unicas}")
print("\nFrecuencia de cada palabra:")
for palabra, frecuencia in frecuencia_palabras.items():
    print(f"{palabra}:{frecuencia}")
#Actividad 6
alumnos = {}
for i in range(3):
    nombre = input(f"nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        while True:
            try:
                nota = float(input(f"nota {j+1} de {nombre}: "))
                notas.append(nota)
                break
            except ValueError:
                print("Ingrese un número válido.")
    alumnos[nombre] = tuple(notas)
print(alumnos)
for nombre, notas in alumnos.items():
    promedio = sum(notas)/len(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}")
#Actividad 7
parcial1 = {1, 2, 3, 4, 5, 6}
parcial2 = {4, 5, 6}
aprobados_ambos = parcial1 & parcial2
print("Estudiantes que aprobaron ambos parciales:")
print(aprobados_ambos)
aprobados_solo_uno = parcial1 ^ parcial2
print("\nEstudiantes que aprobaron solo uno de los dos parciales:")
print(aprobados_solo_uno)
aprobados_total = parcial1 | parcial2
print("\nEstudiantes que aprobaron al menos un parcial:")
print(aprobados_total)
#Actividad 8
stock_productos = {}

def consultar_stock():
    producto = input("Ingrese el nombre del producto: ")
    if producto in stock_productos:
        print(f"El stock de {producto} es: {stock_productos[producto]}")
    else:
        print(f"No se encontró el producto {producto}")

def agregar_stock():
    producto = input("Ingrese el nombre del producto: ")
    if producto in stock_productos:
        try:
            unidades = int(input("Ingrese la cantidad de unidades a agregar: "))
            stock_productos[producto] += unidades
            print(f"Se agregaron {unidades} unidades al stock de {producto}. Nuevo stock: {stock_productos[producto]}")
        except ValueError:
            print("Ingrese un número válido.")
    else:
        print(f"No se encontró el producto {producto}")

def agregar_producto():
    producto = input("Ingrese el nombre del producto: ")
    if producto not in stock_productos:
        try:
            unidades = int(input("Ingrese la cantidad de unidades iniciales: "))
            stock_productos[producto] = unidades
            print(f"Se agregó el producto {producto} con un stock de {unidades} unidades.")
        except ValueError:
            print("Ingrese un número válido.")
    else:
        print(f"El producto {producto} ya existe.")

while True:
    print("\nMenú de opciones:")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades al stock de un producto")
    print("3. Agregar un nuevo producto")
    print("4. Salir")
    opcion = input("Ingrese la opcion deseada: ")
    if opcion == "1":
        consultar_stock()
    elif opcion == "2":
        agregar_stock()
    elif opcion == "3":
        agregar_producto()
    elif opcion == "4":
        break
    else:
        print("Opcion invalida")
#Actividad 9
agenda = {}

def agregar_evento():
    dia = input("Ingrese el día (lunes, martes, miércoles, jueves, viernes, sábado, domingo): ")
    hora = input("Ingrese la hora (HH:MM): ")
    evento = input("Ingrese el evento: ")
    agenda[(dia, hora)] = evento
    print(f"Se agregó el evento '{evento}' el {dia} a las {hora}.")

def consultar_evento():
    dia = input("Ingrese el día (lunes, martes, miércoles, jueves, viernes, sábado, domingo): ")
    hora = input("Ingrese la hora (HH:MM): ")
    if (dia, hora) in agenda:
        print(f"El {dia} a las {hora} tienes: {agenda[(dia, hora)]}")
    else:
        print(f"No hay eventos programados para el {dia} a las {hora}.")

def mostrar_eventos():
    if agenda:
        print("Eventos programados:")
        for (dia, hora), evento in agenda.items():
            print(f"{dia} a las {hora}: {evento}")
    else:
        print("No hay eventos programados.")

def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar evento")
        print("2. Consultar evento")
        print("3. Mostrar todos los eventos")
        print("4. Salir")
        opcion = input("Ingrese la opción deseada: ")
        
        if opcion == "1":
            agregar_evento()
        elif opcion == "2":
            consultar_evento()
        elif opcion == "3":
            mostrar_eventos()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
#Actividad 10
paises_capitales = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Uruguay": "Montevideo", 
"Brasil": "Río de Janeiro"}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print(capitales_paises)