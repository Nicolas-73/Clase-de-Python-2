productos = [
    {"nombre": "laptop", "precio": 2499.99, "stock": 15},
    {"nombre": "Mouse", "precio": 45.50, "stock": 30},
    {"nombre": "Teclado", "precio": 120.00, "stock": 8},
    {"nombre": "Parlante", "precio": 75.00, "stock": 20}
]

# Mostrar solo los productos con precio menor a S/.100
for producto in productos:
    # {"nombre": "laptop", "precio": 2499.99, "stock": 15},
    if producto["precio"] < 100:
        print(producto["nombre"])

#Mostrar solo los que tienen stock menor a 10
for producto in productos:
    if producto["stock"] < 10:
        print(f"Productos con poco stock: {producto["nombre"]}")

# Encuentra el producto más caro
más_caro = productos[0]
for producto in productos:
    if producto["precio"] > más_caro["precio"]:
        más_caro = producto
print(f"El producto más caro: {más_caro["nombre"]}")

# Crear una lista de nombres de productos con más de 10 unidades
producto_stock = []
for producto in productos:
    if producto["stock"] > 10:
        producto_stock.append(producto["nombre"])
print(producto_stock)