edad = int(input("¿Cuántos años tienes?")) # 18 int
tiene_DNI = input("¿Tienes DNI? (S/N)")

if not tiene_DNI == "S":
    print("No puedes votar.")
elif edad < 16:
    print("No puedes votar, eres menor de edad.")
elif edad <= 17:
    print("Voto optativo.")
elif edad <= 69:
    print("Voto obligatorio.")
else:
    print("Voto optativo, por tu edad mayor de 70.")