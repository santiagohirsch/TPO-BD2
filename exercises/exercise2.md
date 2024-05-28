# Ejercicio 2 - Neo4j

## Configuracion BD

Para configurar la base de datos para la resolucion de este ejercicio nos dirigimos a un [sandbox en blanco](https://sandbox.neo4j.com/) provisto por Neo4j.

### Generacion BD

Para generar la base de grafos en cuestión, ejecutar el comando 

```sh
    :play northwind-graph 
```
desde la interfaz web de Neo4J.

### Carga BD

Para cargar la base de datos generada ejecutar los siguientes comandos:

**1. Carga de los productos**
   
```sh
    LOAD CSV WITH HEADERS FROM "https://data.neo4j.com/northwind/products.csv" AS row
    CREATE (n:Product)
    SET n = row,
    n.unitPrice = toFloat(row.unitPrice),
    n.unitsInStock = toInteger(row.unitsInStock), n.unitsOnOrder = toInteger(row.unitsOnOrder),
    n.reorderLevel = toInteger(row.reorderLevel), n.discontinued = (row.discontinued <> "0")
```

**2. Carga de las categorías**

```sh
    LOAD CSV WITH HEADERS FROM "https://data.neo4j.com/northwind/categories.csv" AS row
    CREATE (n:Category)
    SET n = row
```

**3. Carga de los proveedores**

```sh
    LOAD CSV WITH HEADERS FROM "https://data.neo4j.com/northwind/suppliers.csv" AS row
    CREATE (n:Supplier)
    SET n = row
```

### Creación de relaciones

Para crear las relaciones entre los nodos de la base de datos ejecutar los siguientes comandos:

**1. Relación _PART\_OF_**

Con el siguiente comando creamos la relación _PART\_OF_ entre los **productos** y las **categorías**. En donde un **producto** es _PART\_OF_ de una **categoria**.

```sh
    MATCH (p:Product),(c:Category)
    WHERE p.categoryID = c.categoryID
    CREATE (p)-[:PART_OF]->(c)
```

**2. Relación _SUPPLIES_**

Con el siguiente comando creamos la relación _SUPPLIES_ entre los **productos** y los **proveedores**. En donde un **proveedores** _SUPPLIES_ uno o más **productos**.

```sh
    MATCH (p:Product),(s:Supplier)
    WHERE p.supplierID = s.supplierID
    CREATE (s)-[:SUPPLIES]->(p)
```

## Consultas

### Item a

¿Cuántos productos hay en la base?

Para responder esta consulta se ejecuta el siguiente comando en la interfaz de Neo4j:

```sh
    match (p:Product) 
    return count(p) as NumberOfProducts
```

### Item b

¿Cuánto cuesta el “Queso Cabrales”?

Para responder esta consulta se ejecuta el siguiente comando en la interfaz de Neo4j:

```sh
    match (p:Product) {productName: "Queso Cabrales"}
    return p.unitPrice as QuesoCabralesPrice
```

### Item c

¿Cuántos productos pertenecen a la categoría “Condiments”?

Para responder esta consulta se ejecuta el siguiente comando en la interfaz de Neo4j:

```sh
    match (p:Product)-[:PART_OF]->(c:Category {categoryName:"Condiments"}) 
    return count(p) as CondimentsProductsCount
```

### Item d

Del conjunto de productos que ofrecen los proveedores de “UK”, 
¿Cuál es el nombre y el precio unitario de los tres productos más caros?

Para responder esta consulta se ejecuta el siguiente comando en la interfaz de Neo4j:

```sh
    match (s:Supplier {country:"UK"})-[:SUPPLIES]->(p:Product) 
    return p.productName as ProductName, p.unitPrice as UnitPrice 
    order by p.unitPrice 
    desc limit 3 
```
