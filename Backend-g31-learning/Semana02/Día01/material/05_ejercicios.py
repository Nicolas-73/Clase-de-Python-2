# ALMACEN
# Es una tienda de productos, controlar el stock de 
# productos, si el stock es 0, no se puede vender
# Debo desarrollar funcinoes que me permitar
# automtizar el proceso

productos = [
    {"id": 1, "nombre": "Coca Cola", "stock": 10, "precio": 15},
    {"id": 2, "nombre": "Pepsi", "stock": 1, "precio": 12},
    {"id": 3, "nombre": "Fanta", "stock": 0, "precio": 10},
    {"id": 4, "nombre": "Sprite", "stock": 5, "precio": 14},
    {"id": 5, "nombre": "Agua", "stock": 20, "precio": 8}
]

# 01. Crear una funcion llamada buscar_producto, que reciba el id y
# devuelva el producto
def buscar_producto(id):
    try:
        for producto in productos:
            if producto["id"] == id:
                return producto
    except Exception:
        print("Error encontrado")
# 02. Crear una funcion llamada vender_producto, que reciba el id y la cantidad
# Si el stock es suficiente, se debe restar la cantidad vendida al stock y 
# retornar el precio total de la venta
def veder_producto(id, cantidad):
    producto_encontrado = buscar_producto(id)

    if cantidad > producto_encontrado["stock"]:
        print("Stock insuficiente")
        return # Es para señalar el fin de la ejecución de una función

    # Actualización de la nueva cantidad - Stock
    nueva_cantidad = producto_encontrado["stock"] - cantidad

    # Recorrido el arreglo para actualizar el STOCK
    for producto in productos:
        if producto["id"] == id:
            producto["stock"] = nueva_cantidad

    total = producto_encontrado["precio"] * cantidad
    return total
# 03. Crear una funcion llamada mostrar_productos, que muestre los producto
# con stock menor a 5.
def mostrar_productos():
    for producto in productos:
        if producto["stock"] < 5:
            print(f"{producto["nombre"]} - {producto["stock"]} - {producto["precio"]}")