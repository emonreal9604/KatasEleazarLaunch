# Ejercicio 1
# Función para leer 3 tanques de combustible y muestre el promedio

def generate_report(main_tank, external_tank, hydrogen_tank):
    total_average = (main_tank + external_tank + hydrogen_tank) / 3
    return f"""Fuel Report:
    Total Average: {total_average}%
    Main tank: {main_tank}%
    External tank: {external_tank}%
    Hydrogen tank: {hydrogen_tank}% 
    """


# Llamamos a la función que genera el reporte print(funcion(tanque1, tanque2, tanque3))
print(generate_report(80, 70, 85))
# Función promedio


def average(values):
    total = sum(values)
    number_of_items = len(values)
    return total / number_of_items


# Test the averaging function with a list of integers:
average([80, 85, 81])
# Actualiza la función


def generate_report(main_tank, external_tank, hydrogen_tank):
    return f"""Fuel Report:
    Total Average: {average([main_tank, external_tank, hydrogen_tank])}%
    Main tank: {main_tank}%
    External tank: {external_tank}%
    Hydrogen tank: {hydrogen_tank}% 
    """


# Call the updated function again with different values
print(generate_report(88, 76, 70))
###################################################
# Ejercicio 2
# Función con un informe preciso de la misión. Considera hora de prelanzamiento, tiempo de vuelo, destino, tanque externo y tanque interno


def mission_report(pre_launch_time, flight_time, destination, external_tank, main_tank):
    return f"""
    Mission to {destination}
    Total travel time: {pre_launch_time + flight_time} minutes
    Total fuel left: {external_tank + main_tank} gallons
    """


print(mission_report(14, 51, "Moon", 200000, 300000))
# Escribe tu nueva función de reporte considerando lo anterior


def mission_report(destination, *minutes, **fuel_reservoirs):
    return f"""
    Mission to {destination}
    Total travel time: {sum(minutes)} minutes
    Total fuel left: {sum(fuel_reservoirs.values())}
    """


print(mission_report("Moon", 10, 15, 51, main=300000, external=200000))
# Escribe tu nueva función


def mission_report(destination, *minutes, **fuel_reservoirs):
    main_report = f"""
    Mission to {destination}
    Total travel time: {sum(minutes)} minutes
    Total fuel left: {sum(fuel_reservoirs.values())}
    """
    for tank_name, gallons in fuel_reservoirs.items():
        main_report += f"{tank_name} tank --> {gallons} gallons left\n"
    return main_report


print(mission_report("Moon", 8, 11, 55, main=300000, external=200000))
