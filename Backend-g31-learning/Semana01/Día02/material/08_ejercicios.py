clientes = [
    {"nombre": "Ana", "deuda": 150.00, "dias_atraso": 45},
    {"nombre": "Luis", "deuda": 0, "dias_atraso": 0},
    {"nombre": "Sofia", "deuda": 320.50, "dias_atraso": 60},
    {"nombre": "Carlos", "deuda": 75.00, "dias_atraso": 15},
    {"nombre": "Marta", "deuda": 0, "dias_atraso": 0},
]

clientes_morosos = []
morosos_graves = []

for cliente in clientes:
    if cliente["deuda"] > 0:
        clientes_morosos.append(cliente["nombre"])
    if cliente["deuda"] > 100 and cliente["dias_atraso"] > 30:
        morosos_graves.append(cliente["nombre"])