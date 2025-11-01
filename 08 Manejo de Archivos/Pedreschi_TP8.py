#Actividad 1
with open("productos.txt", "w") as archivo:
    archivo.write("Manzana,1.50,10\n")
    archivo.write("Leche,2.00,5\n")
    archivo.write("Pan,0.50,20\n")


#Actividad 2
archivo = "productos.txt" 
def leer_productos(archivo):
    try:
        with open(archivo, "r") as file:
            for linea in file:
                linea = linea.strip()
                if linea:
                    producto = linea.split(",")
                    nombre = producto[0]
                    precio = float(producto[1])
                    cantidad = int(producto[2])
                    print(f"Producto: {nombre} | Precio: ${precio:.2f} | Cantidad: {cantidad}")
    except FileNotFoundError:
        print("No existe el archivo")
leer_productos("productos.txt")


#Actividad 3
def agregar_producto(archivo):
    nombre = input("Ingrese el nombre del producto: ")
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            break
        except ValueError:
            print("Precio inválido. Por favor, ingrese un número.")
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                break
        except ValueError:
            print("Cantidad inválida. Por favor, ingrese un número entero.")
    with open(archivo, "a") as file:
        file.write(f"{nombre},{precio},{cantidad}\n")
    print("Producto agregado con éxito.")
agregar_producto("productos.txt")


#Actividad 4
def cargar_productos(archivo):
    productos = []
    try:
        with open(archivo, "r") as file:
            for linea in file:
                linea = linea.strip()
                if linea:
                    producto = linea.split(",")
                    productos.append({
                        "nombre": producto[0],
                        "precio": float(producto[1]),
                        "cantidad": int(producto[2])
                    })
    except FileNotFoundError:
        print("El archivo no existe")
    return productos
productos = cargar_productos(archivo)
print(productos)

#Actividad 5
def buscar_producto(productos):
    nombre = input("Ingrese el nombre del producto a buscar: ")
    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']:.2f} | Cantidad: {producto['cantidad']}")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")
buscar_producto(productos)


#Actividad 6
def guardar_productos(archivo, productos):
    with open(archivo, "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Productos guardados con éxito.")
guardar_productos(archivo,productos)