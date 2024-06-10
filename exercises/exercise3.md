# Ejercicio 3 - Redis

## Instalación y conexion

Para utilizar Redis se deben seguir los siguientes pasos:

1. Instalar Docker Desktop for Windows o for Mac o Docker Engine en Linux
2. Para descargar la versión oficial de Redis: 

```sh
    docker pull redis
```

3. Levantar el contenedor: 

```sh
    docker run --name Myredis -p 6379:6379 -d redis
```

4. Para levantar un Shell bash dentro del contenedor: 

```sh
    docker exec -it Myredis bash
```

5. Para apagar el contenedor con: docker stop Myredis
6. Para iniciarla nuevamente: docker start Myredis

Una vez que se levanta el Shell bash dentro del contenedor se debe instalar `Python`. Para lograr esto se deben seguir los siguientes pasos:

1. Actualizar la lista de paquetes: 

```sh
    apt-get update
```

2. Instalar `Python`:

```sh
    apt-get install -y python3
```

3. Instalar `redis`:

```sh
    apt-get install python3-redis
```

## Resolución

### Importación de datasets y scripts

Para importar el csv `bataxi.csv` y el script `exercise3.py` al contenedor se ejecutaron los siguientes comandos (una vez ya creada la [conexion al contenedor](#instalación-y-conexion) y desde una terminal local):

```sh
    docker cp ./data/bataxi.csv Myredis:/bataxi.csv
    docker cp ./scripts/exercise3/exercise3.py Myredis:exercise3.py
```

### Items a - d

Para la resolucion de los items a - d, se ejecuta el script `exercise3` (previamente [importado al contenedor](#instalación-y-conexion)):

1. Nos dirigimos al directiorio en donde se encuentran los [datasets y scripts](#importación-de-datasets-y-scripts):

```sh
    cd ..
```

2. Le otorgamos permisos de ejecución al script:

```sh
    chmod u+x ./exercise3.py
```

3. Ejecutamos el script:

```sh
    ./exercise3.py
```

### Item e

¿Sobre qué estructura de Redis trabaja el GeoADD?

GEOADD utiliza la estructura de datos de Redis llamada 'sorted set'.