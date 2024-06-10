#! /usr/bin/env python3
import redis
import csv

redis_db = redis.StrictRedis(host='localhost', port=6379, db=0)

def item_a(csv_file):
    print("a. Importar los datos del archivo a Redis")
    with open(csv_file, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id_viaje = row['id_viaje_r']
            origen_latitud = float(row['origen_viaje_x'])
            origen_longitud = float(row['origen_viaje_y'])
            redis_db.geoadd("bataxi", (origen_latitud, origen_longitud, id_viaje))
    print("Datos importados correctamente\n\n")

def item_b():      
    print("b. ¿Cuántos viajes se generaron a 1 km de distancia de estos 3 lugares?")
    print("Parque Chas, UTN y ITBA Madero")   
    places = [
        {"place": "Parque Chas", "lon": -58.479258, "lat": -34.582497},
        {"place": "UTN", "lon": -58.468606, "lat": -34.658304},
        {"place": "ITBA Madero", "lon": -58.367862, "lat": -34.602938}
    ]

    for place in places:
        count = len(redis_db.georadius("bataxi", place['lon'], place['lat'], 1, unit='km'))
        print(f"Viajes a 1 km de {place['place']}: {count}")
    print("\n")

def item_c():
    print("c. ¿Cuántas KEYS hay en la base de datos Redis?")
    keys_count = len(redis_db.keys('*'))
    print(f"Número de keys en Redis: {keys_count}\n\n")

def item_d():
    print("d. ¿Cuántos miembros tiene la key 'bataxi'?")
    members_count = redis_db.zcard('bataxi')
    print(f"Número de miembros en 'bataxi': {members_count}")


item_a('./bataxi.csv')
item_b()
item_c()
item_d()
