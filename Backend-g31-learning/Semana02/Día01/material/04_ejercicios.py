# def pedir_entero(mensaje):
#     try:
#         número = int(input(mensaje))
#         return número
#     except Exception:
#         print("Esto no es un número")

# edad = pedir_entero("¿Cuántos años tienes?")
# print(f"Tienes {edad} años")

def pedir_nota(mensaje):
    try:
        nota = int(input(mensaje))
    except ValueError:
        print ("El dato ingresado no es un número")
        return
    if nota > 20 or nota < 0:
        print("La nota no puede ser mayor a 20 ni menor a 0")
        return
    return nota

nota1 = pedir_nota("Introduce tu nota")

print(nota1)