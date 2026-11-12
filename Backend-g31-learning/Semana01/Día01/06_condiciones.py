# Condicionales
# if, else, elif

# [Regla de oro]: la identación y el orden

# Una persona quiere postular a la presidencia del Perú
# Requisito, debe de contor con más de 35 años y debe ser peruano de nacimiento

nombre = "Elvis"
edad = 38
peruano = True

if edad >= 35 and peruano == True:
    print(f"Sr {nombre}, usted es aptto para postularse como presidente.")

else:
    print(f" Sr {nombre}, usted NO está apto.")



es_fin_de_semana = False
# Un if solo se va a ejecutar cuando la condición es verdadera
# True
if not es_fin_de_semana:
    print("No es fin de semana")

# Ternario en Js
# CONDICIÓN ? SI : NO
# Ternario en Python
# SI if CONDICIÓN else NO

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)