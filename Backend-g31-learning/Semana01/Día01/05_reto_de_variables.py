# RETO 01
# Resultado esperado sig.
# nombre = "Arnold"
# edad = 30

# RESULTADO EN TERMINAL
# Hola soy --- tengo -- años vivo en -- y programo en ---
# print(f"Hola {Variable}")
# Hola, soy Arnold es de tipo ... str
# El dato 30 es de tipo ... int
# Naciste en el año 1996

nombre = input("¿Cuál es tu nombre?")
edad = input("¿Cúal es tu edad?")
ciudad = input("¿Cuál es tu ciudad?")
lenguaje = input("¿Cuál es tu lenguaje favorito?")

print(f"Hola soy {nombre}, tengo {edad} años, vivo en {ciudad} y programo en {lenguaje}")

print(nombre, type(nombre))
print(edad, type(edad))

fecha_de_nacimiento = 2026 - int(edad)
print(f"Tu año de nacimiento aproximado es el {fecha_de_nacimiento}")