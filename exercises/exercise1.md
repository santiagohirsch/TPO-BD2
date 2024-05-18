# Ejercicio 1

## Instalación y conexion

Para utilizar MongoDB se deben seguir los siguientes pasos:

1. Instalar Docker Desktop for Windows o for Mac o Docker Engine en Linux
2. Para descargar la versión oficial de MongoDB: docker pull mongo
3. Levantar el contenedor: docker run --name Mymongo –p 27017:27017 -d mongo
4. Para levantar un Shell bash dentro del contenedor: docker exec -it Mymongo bash
5. Para apagar el contenedor con: docker stop Mymongo
6. Para iniciarla nuevamente: docker start Mymongo

### Item a

Para cargar el csv a la base de datos se ejecutaron los siguientes comandos (una vez ya creada la [conexion al contenedor](#instalación-y-conexion)):

1. Primero se copia el csv al contenedor

```sh
    docker cp ./data/albumlist.csv Mymongo:/files
```

2. Luego, se utiliza el comando [mongoimport](https://www.mongodb.com/docs/database-tools/mongoimport/) para importar el csv a la base de datos:

```sh
    mongoimport --db <nombre_de_la_base_de_datos> --collection <nombre_de_la_coleccion> --type csv --headerline --file files
```

### Item b

Cuente la cantidad de álbumes por año y ordénelos de manera descendente (mostrando los años con mayor cantidad de álbumes al principio).

Para lograr esto se ejecuta el siguiente comando desde la terminal de MongoDB:

```sh
    db.<nombre_de_la_coleccion>.aggregate([
        {
            $group: {
                _id: "$Year",
                count: { $sum: 1 }
            }
        },
        {
            $sort: { count: -1 }
        }
    ])
```

> Aclaracion: En el comando, se debe reemplazar <nombre_de_la_coleccion> con el nombre de la coleccion elegida en el [Item a](#item-a)

### Item c

A cada documento, agregarle un nuevo atributo llamado 'score' que sea 501-Number.

Para lograr esto se ejecuta el siguiente comando desde la terminal de MongoDB:

```sh
    db.<nombre_de_la_coleccion>.find().forEach(function(album) {
        var rank = album.Number;
        var score = 501 - rank;
        db.<nombre_de_la_coleccion>.updateOne(
            { _id: album._id },
            { $set: { score: score } }
        );
    });
```

> Aclaracion: En el comando, se debe reemplazar <nombre_de_la_coleccion> con el nombre de la coleccion elegida en el [Item a](#item-a)

### Item d

Realice una consulta que muestre el 'score' de cada artista.

Para lograr esto se ejecuta el siguiente comando desde la terminal de MongoDB:

```sh
    db.<nombre_de_la_coleccion>.aggregate([
        {
            $group: {
                _id: "$Artist",
                Score: { $sum: "$score" }
            }
        },
        {
            $sort: { Score: -1 }
        }
    ])  
```

> Aclaracion: En el comando, se debe reemplazar <nombre_de_la_coleccion> con el nombre de la coleccion elegida en el [Item a](#item-a)

