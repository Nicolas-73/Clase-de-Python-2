import random

class Tragamonedas:
    def __init__(self, nombre, créditos):
        self.nombre = nombre
        self.créditos = créditos
        self.créditos_usados = 0
        self.ganancia_total = 0

    def mostrar(self):
        estado = f"{self.créditos} créditos." if self.créditos > 0 else "No tienes créditos."
        print(f"{self.nombre} - {estado}")

    def girar(self):
        símbolos = ["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"]
        resultado = []
        for i in range(3):
            índice = random.randint(0, len(símbolos) - 1)
            resultado.append(símbolos[índice])
        print(resultado)
        return resultado

    def jugar(self, apuesta):
        if self.créditos == 0:
            print("No hay créditos en esta máquina.")
            return False
        if apuesta > self.créditos:
            print(f"No tienes suficientes créditos, solo dispones de {self.créditos}.")
            return False

        self.créditos = self.créditos - apuesta
        self.créditos_usados = self.créditos_usados + apuesta
        resultadito = self.girar()

        if resultadito[0] == resultadito[1] == resultadito[2]:
            premio = apuesta * 10
            print(f"¡Ganaste {premio} créditos!")
            self.créditos = self.créditos + premio
            self.ganancia_total = self.ganancia_total + premio
        elif resultadito[0] == resultadito[1] or resultadito[0] == resultadito[2] or resultadito[1] == resultadito[2]:
            premio = apuesta * 2
            print(f"¡Ganaste {premio} créditos!")
            self.créditos = self.créditos + premio
            self.ganancia_total = self.ganancia_total + premio
        else:
            print("Perdiste.")
        return True

    def estadísticas(self):
        print(f"\n--- {self.nombre} ---")
        print(f"Créditos apostados: {self.créditos_usados} | Créditos ganados: {self.ganancia_total}")
        balance = self.ganancia_total - self.créditos_usados
        signo = "+" if balance >= 0 else ""
        print(f"Balance: {signo} {balance}")
        print(f"Tienes {self.créditos} créditos restantes.")


class Tragamonedas_La_Frutal(Tragamonedas):
    def __init__(self, nombre, créditos):
        super().__init__(nombre, créditos)

    def girar(self):
        símbolos = ["🍒", "🍋", "🍊", "🍎", "🍍", "🍇"]
        resultado = []
        for i in range(3):
            índice = random.randint(0, len(símbolos) - 1)
            resultado.append(símbolos[índice])
        print(resultado)
        return resultado


class Tragamonedas_La_Siete(Tragamonedas):
    def __init__(self, nombre, créditos):
        super().__init__(nombre, créditos)

    def girar(self):
        símbolos = ["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"]
        resultado = []
        for i in range(3):
            índice = random.randint(0, len(símbolos) - 1)
            resultado.append(símbolos[índice])
        print(resultado)
        return resultado

    def jugar(self, apuesta):
        if self.créditos == 0:
            print("No hay créditos en esta máquina.")
            return False
        if apuesta > self.créditos:
            print(f"No tienes suficientes créditos, solo dispones de {self.créditos}.")
            return False

        self.créditos = self.créditos - apuesta
        self.créditos_usados = self.créditos_usados + apuesta
        resultadito = self.girar()
        tiene_7 = "7️⃣" in resultadito

        if resultadito[0] == resultadito[1] == resultadito[2]:
            premio = apuesta * 15
            print(f"¡Felicidades, ganaste {premio} créditos!")
            self.créditos = self.créditos + premio
            self.ganancia_total = self.ganancia_total + premio
        elif resultadito[0] == resultadito[1] or resultadito[0] == resultadito[2] or resultadito[1] == resultadito[2]:
            premio = apuesta * 3
            print(f"Ganaste {premio} créditos.")
            self.créditos = self.créditos + premio
            self.ganancia_total = self.ganancia_total + premio
        elif tiene_7:
            print("¡Salió La Siete! Recuperas tu apuesta.")
            self.créditos = self.créditos + apuesta
        else:
            print(f"Perdiste {apuesta} créditos.")
        return True


class Tragamonedas_Jackpot_City(Tragamonedas):
    def __init__(self, nombre, créditos):
        super().__init__(nombre, créditos)

    def girar(self):
        símbolos = ["💰", "👑", "💎", "💲", "🪙", "⭐", "🪎", "💵", "🔔"]
        resultado = []
        for i in range(3):
            índice = random.randint(0, len(símbolos) - 1)
            resultado.append(símbolos[índice])
        print(resultado)
        return resultado

    def jugar(self, apuesta):
        if self.créditos == 0:
            print("No hay créditos en esta máquina.")
            return False
        if apuesta > self.créditos:
            print(f"No tienes suficientes créditos, solo dispones de {self.créditos}.")
            return False

        self.créditos = self.créditos - apuesta
        self.créditos_usados = self.créditos_usados + apuesta
        resultadito = self.girar()
        
        # Evaluamos primero el premio especial de 3 estrellas
        triple_estrella = resultadito[0] == resultadito[1] == resultadito[2] == "⭐"

        if triple_estrella:
            premio = apuesta * 100
            print(f"¡Eres la estrella del casino! ¡Ganaste {premio} créditos!")
            self.créditos = self.créditos + premio
            self.ganancia_total = self.ganancia_total + premio
        elif resultadito[0] == resultadito[1] == resultadito[2]:
            premio = apuesta * 20
            print(f"¡Felicidades, ganaste {premio} créditos!")
            self.créditos = self.créditos + premio
            self.ganancia_total = self.ganancia_total + premio
        elif resultadito[0] == resultadito[1] or resultadito[0] == resultadito[2] or resultadito[1] == resultadito[2]:
            premio = apuesta * 5
            print(f"Ganaste {premio} créditos.")
            self.créditos = self.créditos + premio
            self.ganancia_total = self.ganancia_total + premio
        else:
            print(f"Perdiste {apuesta} créditos.")
        return True


def seleccionar_máquina(máquina):
    while máquina.créditos > 0:
        print("-" * 35)
        máquina.mostrar()
        try:
            apuesta = int(input("¿Cuántos créditos apuestas? (Ingresa 0 para volver al menú): "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if apuesta == 0:
            break
        
        máquina.jugar(apuesta)


máquinas = [
    Tragamonedas_La_Frutal("La Frutal", 200),
    Tragamonedas_La_Siete("La Siete", 150),
    Tragamonedas_Jackpot_City("Jackpot City", 100),
]

while True:
    print("\n" + "=" * 35)
    print("⭐ Casino ⭐")
    print("=" * 35)

    for i, m in enumerate(máquinas, 1):
        cantidad_de_créditos = f"{m.créditos} créditos." if m.créditos > 0 else "Te quedaste sin créditos."
        print(f"{i}. {m.nombre} ({cantidad_de_créditos})")

    print(f"{len(máquinas) + 1}. Mostrar las estadísticas.")
    print(f"{len(máquinas) + 2}. Salir.")

    try:
        opciones = int(input("\n Elige una opción: "))
    except ValueError:
        print("No existe esta opción.")
        continue

    if 1 <= opciones <= len(máquinas):
        máquina = máquinas[opciones - 1]
        if máquina.créditos == 0:
            print("No hay créditos en esta máquina.")
        else:
            seleccionar_máquina(máquina)
    elif opciones == len(máquinas) + 1:
        print("\n Ver las estadísticas del casino")
        print("=" * 35)
        for m in máquinas:
            m.estadísticas()
    elif opciones == len(máquinas) + 2:
        print("\n Muchas gracias por visitar el casino.")
        break
    else:
        print("No existe esta opción.")