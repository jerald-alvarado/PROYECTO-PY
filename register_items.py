almacen = {}

def agregar_articulo():
    bodega = input("Introduzca para que bodega va dirigido el artículo (cocina, licores): ")
    nombre = input("Introduzca el nombre del artículo: ")
    descripcion = input("Introduzca la descripción del artículo: ")
    cantidad = int(input("Introduzca la cantidad en inventario a almacenar del artículo: "))
    almacen[bodega] = {"nombre": nombre, "descripcion": descripcion, "cantidad": cantidad}

def actualizar_cantidad():
    bodega = input("Introduzca para que bodega va dirigido el artículo (cocina, licores): ")
    cantidad = int(input("Introduzca la nueva cantidad en inventario del artículo: "))
    almacen[bodega]["cantidad"] = cantidad

def eliminar_articulo():
    nombre = input("Introduzca el nombre del artículo: ")
    del almacen[nombre]

def mostrar_inventario():
    print("Inventario de la bodega:")
    for bodega, articulo in almacen.items():
        print("Bodega:", bodega)
        print("Nombre:", articulo["nombre"])
        print("Descripción:", articulo["descripcion"])
        print("Cantidad en inventario:", articulo["cantidad"])
        print("--------------------")

while True:
    
    print("Bienvenido al registro de articulos")
    print("1. Agregar un artículo")
    print("2. Actualizar la cantidad de un artículo")
    print("3. Eliminar un artículo")
    print("4. Mostrar el inventario completo")
    print("5. Salir")
    
    opcion = int(input("Introduzca su elección: "))
    if opcion == 1:
        agregar_articulo()
    elif opcion == 2:
        actualizar_cantidad()
    elif opcion == 3:
        eliminar_articulo()
    elif opcion == 4:
        mostrar_inventario()
    elif opcion == 5:
        break

