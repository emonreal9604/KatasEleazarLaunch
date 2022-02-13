planetas = ['Mercury', 'Venus', 'Earth', 'Mars',
            'Jupiter', 'Saturn', 'Uranus', 'Neptune']

print("hay ", len(planetas), " planetas")
# Agregamos a plutón y mostramos el último elemento

planetas.append('Pluto')

print(planetas[-1], 'is the last planet')

###############################
# Ejercicio 2
# Lista de planetas

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']
# Solicitamos el nombre de un planeta *Pista:  input()*
user_planet = input(
    'Please enter the name of the planet (with a capital letter to start)')
# Busca el planeta en la lista

planet_index = planets.index(user_planet)
# Muestra los planetas más cercanos al sol

print('Here are the planets closer than ' + user_planet)
print(planets[0:planet_index])
# Muestra los planetas más lejanos al sol

print('Here are the planets further than ' + user_planet)
print(planets[planet_index + 1:])
