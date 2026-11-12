temperaturas = [22, 31, 28, 35, 18, 40, 27, 33, 15]

temperatura_farenheit = []
temperatura_alta = max(temperaturas)
temperatura_baja = min(temperaturas)
contador = 0
temperatura_promedio = sum(temperaturas)/len(temperaturas)

for c in temperaturas:
    f = c * 9/5 + 32
    temperatura_farenheit.append(f)

    if c > 30:
        contador = contador + 1

print(f"Temperaturas originales (°C): {temperaturas}")
print(f"Temperaturas en Fahrenheit (°F): {temperatura_farenheit}")
print(f"Temperatura más alta: {temperatura_alta}°C")
print(f"Temperatura más baja: {temperatura_baja}°C")
print(f"Cantidad que superaron los 30°C: {contador}")
print(f"Promedio en °C: {temperatura_promedio}")