import csv
import os

# Obtén la ruta del archivo actual
ruta_actual = os.path.dirname(__file__)

# Función para leer datos desde un archivo CSV
def leer_datos_csv(nombre_archivo):
    datos = []
    ruta_archivo = os.path.join(ruta_actual, nombre_archivo)
    if not os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'w', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["nombre", "poblacion", "superficie", "continente"])
    else:
        with open(ruta_archivo, 'r') as archivo:
            lector = csv.reader(archivo)
            try:
                encabezado = next(lector)
                if encabezado != ["nombre", "poblacion", "superficie", "continente"]:
                    respuesta = input("El archivo existente no tiene el formato correcto. ¿Desea reemplazarlo con un archivo nuevo? (s/n): ")
                    if respuesta.lower() == "s":
                        os.remove(ruta_archivo)
                        with open(ruta_archivo, 'w', newline='') as archivo_nuevo:
                            escritor = csv.writer(archivo_nuevo)
                            escritor.writerow(["nombre", "poblacion", "superficie", "continente"])
                    else:
                        print("Saliendo del programa.")
                        exit()
            except StopIteration:
                respuesta = input("El archivo existente está vacío. ¿Desea agregar un encabezado? (s/n): ")
                if respuesta.lower() == "s":
                    os.remove(ruta_archivo)
                    with open(ruta_archivo, 'w', newline='') as archivo_nuevo:
                        escritor = csv.writer(archivo_nuevo)
                        escritor.writerow(["nombre", "poblacion", "superficie", "continente"])
                else:
                    print("Saliendo del programa.")
                    exit()
    
    with open(ruta_archivo, 'r') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila:
                datos.append({
                    'nombre': fila['nombre'],
                    'poblacion': int(fila['poblacion']) if fila['poblacion'] else 0,
                    'superficie': int(fila['superficie']) if fila['superficie'] else 0,
                    'continente': fila['continente']
                })
    return datos


# Función para guardar datos en el archivo CSV
def guardar_datos_csv(nombre_archivo, datos):
    ruta_archivo = os.path.join(ruta_actual, nombre_archivo)
    with open(ruta_archivo, 'w', newline='') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
        escritor.writeheader()
        escritor.writerows(datos)

# Función para agregar un país
def agregar_pais(datos):
    nombre = input("Ingrese el nombre del país: ").title()
    while True:
        try:
            poblacion = int(input("Ingrese la población del país: "))
            break
        except ValueError:
            print("La población debe ser un número entero.")
    while True:
        try:
            superficie = int(input("Ingrese la superficie del país: "))
            break
        except ValueError:
            print("La superficie debe ser un número entero.")
    while True:
        continente = input("Ingrese el continente del país (América, Europa, Asia, África, Oceanía o Antártida): ").title()
        if continente in ["América", "Europa", "Asia", "África", "Oceanía", "Antártida"]:
            break
        else:
            print("Continente inválido. Por favor, intente nuevamente.")
    datos.append({
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    })
    guardar_datos_csv('paises.csv', datos)
    print("País agregado con exito.")

# Función para actualizar los datos de un país
def actualizar_pais(datos):
    nombre = input("Ingrese el nombre del pais a actualizar: ")
    for pais in datos:
        if pais['nombre'] == nombre:
            pais['poblacion'] = int(input("Ingrese la nueva población del país: "))
            pais['superficie'] = int(input("Ingrese la nueva superficie del país: "))
            guardar_datos_csv('paises.csv', datos)
            print("País actualizado con éxito.")
            return
    print("País no encontrado.")


# Función para buscar un país por nombre
def buscar_pais(datos):
    nombre = input("Ingrese el nombre del país a buscar: ")
    resultados = [pais for pais in datos if nombre.lower() in pais['nombre'].lower()]
    if resultados:
        print("Resultados de la búsqueda:")
        for pais in resultados:
            print(f"Nombre del país: {pais['nombre']}")
            print(f"Población: {pais['poblacion']}")
            print(f"Superficie: {pais['superficie']}")
            print(f"Continente: {pais['continente']}")
            print("------------------------")
    else:
        print("No se encontraron resultados.")

# Función para filtrar países por continente
def filtrar_por_continente(datos):
    continente = input("Ingrese el continente a filtrar: ").strip().lower()
    resultados = [pais for pais in datos if pais['continente'].strip().lower() == continente]
    if resultados:
        print("Resultados del filtro:")
        for pais in resultados:
            print(pais['nombre'])
    else:
        print("No se encontraron resultados.")

# Función para ordenar países por nombre
def ordenar_por_nombre(datos):
    datos.sort(key=lambda x: x['nombre'])
    print("Países ordenados por nombre:")
    for pais in datos:
        print(pais['nombre'])

# Función para mostrar estadísticas
def mostrar_estadisticas(datos):
    pais_mayor_poblacion = max(datos, key=lambda x: x['poblacion'])
    pais_menor_poblacion = min(datos, key=lambda x: x['poblacion'])
    promedio_poblacion = sum(pais['poblacion'] for pais in datos) / len(datos)
    promedio_superficie = sum(pais['superficie'] for pais in datos) / len(datos)
    # Cantidad de países por continente
    continentes = {}
    for pais in datos:
        continente = pais['continente']
        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1
    
    print("Estadísticas:")
    print(f"País con mayor población: {pais_mayor_poblacion['nombre']}")
    print(f"País con menor población: {pais_menor_poblacion['nombre']}")
    print(f"Promedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f}")
    print("Cantidad de países por continente:")
    for continente, cantidad in continentes.items():
        print(f"{continente}: {cantidad}")



datos = leer_datos_csv('paises.csv')
while True:
    print("Menú de opciones:")
    print("1. Agregar país")
    print("2. Actualizar país")
    print("3. Buscar país")
    print("4. Filtrar por continente")
    print("5. Ordenar por nombre")
    print("6. Mostrar estadísticas")
    print("7. Salir")
    opcion = input("Ingrese la opción deseada: ")
    if opcion == '1': agregar_pais(datos)
    elif opcion == '2': actualizar_pais(datos)
    elif opcion == '3': buscar_pais(datos)
    elif opcion == '4': filtrar_por_continente(datos)
    elif opcion == '5': ordenar_por_nombre(datos)
    elif opcion == '6': mostrar_estadisticas(datos)
    elif opcion == '7': break
    else: print("Opción inválida. Por favor, intente nuevamente.")

