
# Importamos las librerías

import csv
import json


# Empezamos creando una función "get_equipos" para que recorra el csv y nos devuelva un JSON con los equipos españoles.

def get_equipos():
    
    with open("equiposmod.csv", "r") as csvfile: # Abrimos el csv y lo leemos.
        reader = csv.reader(csvfile, delimiter=",")
        equipos_set = set() # Creamos un conjunto de equipos, al cual se van a ir agregando los nombres de los equipos a medida que recorremos el csv.
        for row in reader:
            equipos_set.add(row[0]) # Aquí es donde se agregan

    return json.dumps(list(equipos_set)) # Y nos devuelve un JSON con los nombres de los equipos.

# Ahora lo mismo pero la función "get_jugadores(A)", donde "A" es un parámetro que es un equipo, y esta función nos devolverá 
# un JSON con los nombres de los jugadores del equipo "A".

def get_jugadores(equipo):
    
    with open("equiposmod.csv", "r") as csvfile: # Abrimos el csv y lo leemos.
        reader = csv.reader(csvfile, delimiter=",")
        jugadores_set =set() #Creamos un set de jugadores donde vamos a ir agregando los nombres de los jugadores.
        for row in reader:
            if row[0] == equipo: # Lo que hacemos es que si el equipo coincide, añadimos el nombre de los jugadores al conjunto.
                jugadores_set.add(row[1])
    return json.dumps(list(jugadores_set))


# Por último comprobamos que ha salido todo bien, probando las funciones.

equipos = get_equipos()
print(equipos)

jugadores = get_jugadores("Real Madrid")
print(jugadores)


