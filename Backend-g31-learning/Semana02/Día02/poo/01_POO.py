# POO => Programación Orientada a Objetos

# Es un paradigma de programación, vamos a organizar nuestro código mediante clases y objetos
# Es representar a los objetos del mundo real, dentro de un programa

# MUNDIAL 2026
nombre1 = "Messi"
edad1 = 37
posicion1 = "Delantero"
equipo1 = "Argentina"

nombre2 = "Mbappe"
edad2 = 27
posicion2 = "Delantero"
equipo2 = "Francia"

# Para solucionar el problema de arriba, usaremos las clases
# ¿Qué es una clase? (PLANO)
# Es una plantlla o molde, que define las características y los métodos (comportamientos)


# ¿Cómo puedo solicitar valores para crear mi clase?
# El Constructor, te va a permitir recibir datos y con esos datos, tú podrás crear tu instancia (objeto)
# Constructor => __init__

class Jugador:
    # La creación de un constructor
    # Regla de oro:
    # Toda función dentro de una clase, su primer argumento es el self
    def __init__(self, nombre, edad, posición, equipo):

        # self = Jugador (a nuestra clase)
        self.nombre = nombre
        self.edad = edad
        self.posición = posición
        self.equipo = equipo

    def correr(self):
        print(f"El jugador {self.nombre} está corriendo")

    def mostrar_info(self):
        # Nombre - Edad años - Posición - Equipo
        print(f"{self.nombre} - {self.edad} años - {self.posición} - {self.equipo}")

    def anotar_gol(self, equipo_rival):
        print(f"El jugador {self.nombre} anotó un gol contra {equipo_rival}")

# Convertir una clase en algo tangible
# Instanciar (Crear un objeto)

messi = Jugador("Lionel Messi", 37, "Delantero", "Argentina")
mbappe = Jugador("Kylian Mbappe", 27, "Dealntero", "Francia")

# Métodos - Funciones
# Una clase no solo tiene datos, sino también puede realizar acciones
# Ejecución de un método
messi.correr()
mbappe.mostrar_info()
mbappe.anotar_gol("Valencia")

# Pilares del POO
# Abstración
# Poliformismo
# Herencia
# Encapsulamiento

# ABSTRACCIÓN
# Extrae las propiedades y métodos de parte de un objeto real

class Equipo:
    def __init__(self, nombre, país):
        self.nombre = nombre
        self.país = país
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
        print(f"Jugador insertado exitosamente")

brasil = Equipo("Selección de Brasil", "Brasil")

ronaldo = Jugador("Ronaldo", 29, "Delantero", "Selección de Brasil")
rivaldo = Jugador("Rivaldo", 28, "Delantero", "Selección de Brasil")
ronaldinho = Jugador("Roanlldiho", 27, "Mediocampista", "Selección de Brasil")

brasil.agregar_jugador(ronaldo)
brasil.agregar_jugador(rivaldo)
brasil.agregar_jugador(ronaldinho)

print(brasil.jugadores)

# POLIMORFISMO
# Una clase puede tomar muchas formas
cristiano_ronaldo = Jugador("Cristiano Ronaldo", 41, "Volante", "Selección de Portugal")
halland = Jugador("Halland", 24, "Delantero", "Selección de Noruega")

# HERENCIA
# La clase padre hereda a la clase hija
# Hereda el comortamiento de las propiedades y los métodos a la clase hija

class JugadorPadre:
    def __init__(self, nombre, edad, equipo):
        self.nombre = nombre
        self.edad = edad
        self.equipo = equipo
    def entrenar(self):
        print(f"Hol estoy entrenando, te saluda {self.nombre}")

#              (Herencia)
class Arquero(JugadorPadre):
    # Nesecitamos estatura y los penalesAtajados
    def __init__(self, nombre, edad, equipo, estatura, penalesAtajados):
        super().__init__(nombre, edad, equipo)
        self.estatura = estatura
        self.penalesAtajados = penalesAtajados

    def atjar(self):
        print(f"Balón atajado por {self.nombre}")


dibu = Arquero("Dibu Martinez", 33, "Argentina", 1.95, 150)

print(dibu.nombre)

dibu.nombre = "Emiliano Martinez"

print(dibu.nombre)