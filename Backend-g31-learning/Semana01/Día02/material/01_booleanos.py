# Los BOOLEANOS
# True y False
# Controlar el flujo de nuestra aplicación

# and
# qQue ambos valores deben ser True

print( True and False) # False
print( True and True) # True

#Solicitar que tenga DNI y ser mayor de edad
# una operación

dni = True
mayor_de_edad = True

if dni and mayor_de_edad:
    print("Adelante. puedes operarte.")
else:
    print("No puedes operarte.")

# or
# Que al menos un valor debe ser True

# Para entrar a la sala VIP
# Tener un amigo promotor ó tener la pulsera verde

amigo_promotor = False
pulsera_verde = True

if amigo_promotor or pulsera_verde:
    print("Adelante, puedes ingresar a la fiesta.")
else:
    print("No puedes ingresar a la fiesta.")