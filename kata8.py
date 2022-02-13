# Ejercicio 1:
# Crea un diccionario llamado planeta con los datos propuestos

planeta = {
    'name': 'Mars',
    'moons': 2
}
# Muestra el nombre del planetaa y el número de lunas que tiene.

print(f'{planeta["name"]} has {planeta["moons"]} moons')
# Agrega la clave circunferencia con los datos proporcionados previamente

planeta['circunferencia (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}
##################################
# Ejercicio 2
# Añade el código para determinar el número de lunas.
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
# Obtenemos la lista de las lunas
# Almacenamos los resultados en una variable moons
moons = planet_moons.values()

# Obtenemos el total de planetas
# Almacenamos los resultados en una variable llamada years
planetas = len(planet_moons.keys())
# Calcula el total_moons agregando todas las lunas
# Almacena su valor en una variable llamada total_moons

total_moons = 0
for moon in moons:
    total_moons = total_moons + moon

# Calcula el promedio dividiendo el total_moons por el número de planetas
average = total_moons / planetas

# Muestra el promedio
print(average)
