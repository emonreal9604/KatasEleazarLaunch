# Añadir el código necesario para crear una variable que guarde la velocidad del asteroide.
# Escribe una expresión de prueba para calcular si necesita una advertencia.
# Agregue las instrucciones que se ejecutarán si la expresión de prueba es true o false.

asteroide = 49
if asteroide > 25:
    print('¡Alerta! ¡Un asteroide se acerca a velocidades peligrosas!')
else:
    print('¡Sigue con tu día!')
# Problema No. 2
# Agrega el código para crear una variable para un asteroide que viaja a 19 km/s
# Escribe varias expresiones de prueba para determinar si puedes ver el rayo de luz desde la tierra
# Agrega las instrucciones que se ejecutarán si las expresiones de prueba son True o False

asteroide = 19
if asteroide > 20:
    print('Look up! ¡Hay una luz mágica en el cielo!')
elif asteroide == 20:
    print('Look up! ¡Hay una luz mágica en el cielo!')
else:
    print('¡Nada que ver aquí!')
# Problema No. 3
# Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
# Para probar el código, prueba con varias velocidades y tamaños
# Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar qué mensaje se debe enviar a Tierra.

velocidad_asteroide = 25
tamano_asteroide = 40
if velocidad_asteroide > 25 and tamano_asteroide > 25:
    print('¡Alerta, Un asteroide muy peligroso viene hacia la Tierra!')
elif velocidad_asteroide >= 20:
    print('Look up! ¡Hay una luz mágica en el cielo!')
elif tamano_asteroide < 25:
    print('Nada que ver aquí :)')
else:
    print('Nada que ver aquí :)')
