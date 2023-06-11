# Test de rendimiento bases de datos Nosql

Desarrollar y utilizar las nuevas aplicaciones de la actualidad ha creado nuevas necesidades en la arquitectura de las bases de datos NoSQL, estas tienen que ser cada vez más ágiles, también requieren un desarrollo cada vez más enfocado a los datos en tiempo real, al igual que cada vez es más necesario que esta tecnología pueda procesar cómodamente impredecibles niveles de escala, velocidad y variabilidad de datos, agregando a todo esto la necesidad de las empresas y organizaciones de innovar rápidamente, operar a cualquier escala, además de cumplir la demanda principal que es la experiencia de usuario.

## Bases de datos NoSql utilizadas

- MongoDB
- Couchbase
- Azure CosmoDB

El patrones de arquitectura de datos NoSQL utilizado fue por documentos

- Una base de datos orientada a documentos está diseñada para gestionar información orientada a documentos o datos semi-estructurados.  Este tipo de bases de datos constituye una de las principales categorías de las llamadas bases de datos NoSQL. 

Las pruebas se hicieron mediante la interfaz de cada base de datos.

- MongoDB: Las pruebas se realizaron en MongoDB Compass.
- En Azure Cosmo DB: Se realizaron en Azure Cosmos DB Emulator
- Couchbase: Se realizaron en el Dashboard de Couchbase Community Server.

## Características Computador:

●	Procesador: Ryzen 7 5800H
●	Ram: 16GB DDR4 3200Mhz
●	Almacenamiento: 512 GB SSD 3000 mb\s

## Metodologia

Se optó por solamente utilizar consultas de lectura en las pruebas, Se repitió 3 veces la misma consulta y se tomó el promedio, se utilizaron 8 cantidades de resultados diferentes para las mediciones. El flujo de trabajo que se utilizó para los conjuntos de datos “Películas” y “Ruta Aviones” fue el siguiente:

1.	1,000 resultados
2.	10,000 resultados
3.	50,000 resultados
4.	100,000 resultados
5.	200,000 resultados
6.	400,000 resultados
7.	600,000 resultados
8.	800,000 resultados

Mientras que para el conjunto de datos “Denue” se utilizaron solamente 6 cantidades diferentes de resultados para las mediciones, esto debido a la cantidad de documentos de este conjunto, ya que es de menor tamaño a los 2 anteriores. El flujo de trabajo fue el siguiente:

1.	1,000 resultados
2.	10,000 resultados
3.	50,000 resultados
4.	100,000 resultados
5.	200,000 resultados
6.	300,000 resultados

La prueba se realizó de manera local, se utilizaron 2 métodos para hacer las pruebas de las bases de datos:

*Test en caliente*
- Las consultas se realizaron de manera consecutiva.
*Test en frío:* 
- Las consultas se realizaron apagando el ordenador cada vez que se realizaba una consulta.
