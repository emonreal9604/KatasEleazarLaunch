# Ejercicio 1


planeta_nuevo = ''
planetas = []


while planeta_nuevo.lower() != 'finalizar':
    if planeta_nuevo:
        planetas.append(planeta_nuevo)
    planeta_nuevo = input('Ingrese el nombre del planeta:\n')

############################################
# Eercicio 2
# imprimimos los planetas ingresados
for i in planetas:
    print(i)
