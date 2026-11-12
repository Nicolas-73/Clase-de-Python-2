class Auto:
    def __init__(self, nroLlantas, color, tipo, marca, nroVentanas):
        self.nroLlantas = nroLlantas
        self.color = color
        self.tipo = tipo
        self.marca = marca
        self.nroVentanas = nroVentanas

sedan = Auto(4, "rojo", "Sedán", "Toyota", 6)
station_wagon = Auto(4, "Azul", "Station Wagon", "Chevrolet", 8)
coupe = Auto(4, "Amarillo", "Coupé", "Ford", 6)

print(f"El vehículo es un {sedan.tipo} de la marca {sedan.marca}; es de color {sedan.color} tiene {sedan.nroLlantas} llantas y {sedan.nroVentanas} ventanas.")

print(f"El vehículo es un {station_wagon.tipo} de la marca {station_wagon.marca}; es de color {station_wagon.color} tiene {station_wagon.nroLlantas} llantas y {station_wagon.nroVentanas} ventanas.")

print(f"El vehículo es un {coupe.tipo} de la marca {coupe.marca}; es de color {coupe.color} tiene {coupe.nroLlantas} llantas y {coupe.nroVentanas} ventanas.")