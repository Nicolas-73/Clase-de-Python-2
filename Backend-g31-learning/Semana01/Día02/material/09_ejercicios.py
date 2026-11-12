# INTERBANK
# El siguiente usuario esta teniendo los siguientes movimientos
movimientos = [
{ "fecha": "2024-01-15", "tipo": "deposito", "monto": 1500.00},
{ "fecha": "2024-01-20", "tipo": "retiro", "monto": 200.00},
{ "fecha": "2024-02-05", "tipo": "deposito", "monto": 500.00},
{ "fecha": "2024-02-10", "tipo": "retiro", "monto": 100.00},
{ "fecha": "2024-02-15", "tipo": "deposito", "monto": 300.00},
{ "fecha": "2024-02-20", "tipo": "retiro", "monto": 50.00},
{ "fecha": "2024-02-25", "tipo": "deposito", "monto": 1000.00 }
]

# 01. Sumar todos los depositos
# 02. Sumar todos los retiros
# 03. Calcular el balance final (depositos - retiros)
# 04. Mostrar el deposito mas grande
# 05. Mostrar el retiro mas grande

# TIPS: Usar el bucle for, usr if, crear variables para acumular valores

depósitos = []
retiros = []

for movimiento in movimientos:
    if movimiento["tipo"] == "deposito":
        depósitos.append(movimiento["monto"])
    else:
        retiros.append(movimiento["monto"])

print(depósitos)
print(f"La suma de los depósitos es: {sum(depósitos)}")
print(f"La suma de los retiros es: {sum(retiros)}")
print(f"El saldo es: {sum(depósitos) - sum(retiros)}")
print(f"El depósito más grande es: {max(depósitos)}")
print(f"El retiro más grande es: {max(retiros)}")