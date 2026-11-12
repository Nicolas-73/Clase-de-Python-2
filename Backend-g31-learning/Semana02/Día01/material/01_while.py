# VIDEOJUEGOS
# Las vidas del juego son solo 3
# Si el usuario pierde una vida, puede seguir jugando
# Pero cuando las vidas sean menores o iguales a 0, el juego se detendrá


# print("Bienvenido a mi videojuego")

# vidas = 3

# while vidas > 0:
#     print(f"Tienes {vidas} vidas")
#     respuesta = input("¿Quieres perder una vida? (s/n)")
#     if respuesta == "s":
#         vidas = vidas -1
#         print("Has perdido una vida")

# print("Fin del juego, no tienes vidas")

# Ejercicio N° 02
# Contraseñas
# El usuario va a iniciar con una contraseña de 0 dígitos
# password = ""
# Tiene que venir un bucle usando while
# Que se ejecutará mientras que la contraseña sea diferente a Python
# Y pedirá al usuario que ingrese la contraseña

password = ""
válido = False

while not válido:
    print("Ingrese la contraseña correcta")
    password = input("Ingresa la contraseña: ")
    if password == "python":
        válido = True
        print("Contraseña Correcta")