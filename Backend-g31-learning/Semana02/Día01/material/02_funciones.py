# def saludar(nombre, apellido):
    # Aquí viene todo mi código
    # print("Hola amigos")
    # print("Un gusto en conocerlos")
    # print(f"Mi nombre es {nombre} {apellido}")

# saludar("Nicolás", "Ticse")
# saludar(apellido="Ticse", nombre="Nicolás")

# def sumar (n1, n2, n3, n4):
#     total = n1 + n2 + n3 + n4
#     return total

# *args
def suma_global(*argument):
    total = 0
    for number in argument:
        total = total +number
    print(total)
    return total

suma_global(10, 5, 100, 3000)


# **kwargs

def calcularBalnce(depósito, retiro):
    print(depósito - retiro)
    return depósito - retiro

cliente = {
    "depósito": 15000,
    "retiro": 3000
}

# calcularBalnce(retiro=cliente["retiro"], depósito=cliente["depósito"])
calcularBalnce(**cliente)