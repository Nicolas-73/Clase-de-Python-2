# Listas - Arrays

notas_alumnos = [15, 18, 19, 8]
lista_de_lista = [[1, 2], ["Calcetín", 4]]

# Muestrame la última notq de tus alumnos
print(notas_alumnos[-1]) # Muestra el último elemento

# Muestrame el 2 que está dentro de lista_de_lista
print(lista_de_lista[0][1]) # 2

frutas = ["manzana", "mango", "uva", "cereza"]

frutas[2] = "piña"

nuevas_frutas = frutas + ["pera", "fresa"]

# ¿Cuántos elementos hay en mi lista?
len(frutas)

# Para insertar un elemento al final de la lista
# append
países = ["USA", "Japón", "Canadá"]
países.append("Bolivia")
países.count("Japón")