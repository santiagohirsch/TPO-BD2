# Ejercicio 1 - MongoDB

## Instalación y conexion

Para utilizar MongoDB se deben seguir los siguientes pasos:

1. Instalar Docker Desktop for Windows o for Mac o Docker Engine en Linux
2. Para descargar la versión oficial de MongoDB: 

```sh
    docker pull mongo
```

3. Levantar el contenedor: 

```sh
    docker run --name Mymongo –p 27017:27017 -d mongo
```

4. Para levantar un Shell bash dentro del contenedor: 

```sh
    docker exec -it Mymongo bash
```

5. Para apagar el contenedor con: 

```sh
    docker stop Mymongo
```

6. Para iniciarla nuevamente: 

```sh
    docker start Mymongo
```

## Resolución

### Importación de datasets y scripts

Para importar el csv `albumlist.csv` y los scripts necesarios para la resolución del ejercicio se ejecuta el script `exercise1_setup.sh` que se encuentra dentro del directorio `scripts/exercise1` (una vez ya creada la [conexion al contenedor](#instalación-y-conexion) y desde una terminal local):

1. Le otorgamos permisos de ejecución al script:

```sh
    chmod u+x ./scripts/exercise1/exercise1_setup.sh
```

2. Ejecutamos el script

```sh
    ./scripts/exercise1/exercise1_setup.sh
```

3. Le otorgamos permisos de ejecución a los scripts importados (desde el Shell bash del contenedor):

```sh
    chmod u+x exercise1_*.sh
```

### Item a

Importe el archivo albumlist.csv (o su versión RAW) a una colección. Este archivo cuenta con el top 500 de álbumes musicales de todos los tiempos según la revista Rolling Stones.

Desde el contenedor, se ejecuta el script `exercise1_a.sh`:

```sh
    ./exercise1_a.sh
```

### Item b

Cuente la cantidad de álbumes por año y ordénelos de manera descendente (mostrando los años con mayor cantidad de álbumes al principio).

Desde el contenedor, se ejecuta el script `exercise1_b.sh`:

```sh
    ./exercise1_b.sh
```

### Item c

A cada documento, agregarle un nuevo atributo llamado 'score' que sea 501-Number.

Desde el contenedor, se ejecuta el script `exercise1_c.sh`:

```sh
    ./exercise1_c.sh
```

### Item d

Realice una consulta que muestre el 'score' de cada artista.

Desde el contenedor, se ejecuta el script `exercise1_d.sh`:

```sh
    ./exercise1_d.sh
```