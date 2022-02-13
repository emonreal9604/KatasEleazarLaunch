# Crear variables para almacenar las dos distancias
# ¡Asegúrate de quitar las comas!

saturno = 1433500000
neptuno = 778547200
# Calcular la distancia entre planetas

distancia_km = neptuno - saturno
print(distancia_km)

distance_millas = distancia_km * 1.609344
print(distance_millas)
##################################
# Ejercicio 2
# Almacenar las entradas del usuario
first_planet = input(
    'Introduzca la distancia del sol para el primer planeta en KM: ')
second_planet = input(
    'Introduzca la distancia desde el sol para el segundo planeta en KM: ')
# Convierte las cadenas de ambos planetas a números enteros
first_planet = int(first_planet)
second_planet = int(second_planet)
# Realizar el cálculo y determinar el valor absoluto
distance_km = second_planet - first_planet
print(distance_km)

# Convertir de KM a Millas
distance_mi = distance_km * 1.609344
print(distance_mi)
