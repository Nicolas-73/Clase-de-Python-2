# Try - Except
# Vamos a lograr manipular los errores
try:
    número = int(input("Ingresa un número"))
    if número < 0:
        raise Exception("No se permiten números negativos")
    print(f"Tu número es {número}")
except Exception:
    print("Tuvimos un erroe con el número")
finally:
    print("Fin del programa")

# Capturar errores específicos
# ValueError => El valor tiene un formato incorrecto
# ZeroDivisionError => Se intenta dividir entre 0
# NameError => Se i está usando una variable no creada
# ImportError => No se puede importar un módulo
# Exception => Un salvavidas cuando no conoces el errr específico

