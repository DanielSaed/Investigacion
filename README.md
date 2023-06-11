# Test de rendimiento bases de datos Nosql

Desarrollar y utilizar las nuevas aplicaciones de la actualidad ha creado nuevas necesidades en la arquitectura de las bases de datos NoSQL, estas tienen que ser cada vez más ágiles, también requieren un desarrollo cada vez más enfocado a los datos en tiempo real, al igual que cada vez es más necesario que esta tecnología pueda procesar cómodamente impredecibles niveles de escala, velocidad y variabilidad de datos, agregando a todo esto la necesidad de las empresas y organizaciones de innovar rápidamente, operar a cualquier escala, además de cumplir la demanda principal que es la experiencia de usuario.

## Bases de datos NoSql utilizadas

- MongoDB
- Couchbase
- Azure CosmoDB

*Todas la bases de datos anteriores utilizan el patron de arquitectura de datos por documentos.*

Las pruebas se hicieron mediante la interfaz de cada base de datos.

- MongoDB:  MongoDB Compass.
- En Azure CosmosDB: Azure Cosmos DB Emulator
- Couchbase: Dashboard de Couchbase Community Server.

## Características Computador:

●	Procesador: Ryzen 7 5800H
●	Ram: 16GB DDR4 3200Mhz
●	Almacenamiento: 512 GB SSD 3000 mb\s

## Datasets utilizados:

 <table align="middle">
  <tr align="middle">
    <td><img src="https://github.com/DanielSaed/Investigacion/blob/main/img-github/tabla.png" width=600 height=300 align="middle"></td>
  </tr>
 </table>
 
## Metodologia

**Metodologia Seguida en la investigacion**

<table align="middle">
  <tr>
    <td><img src="https://github.com/DanielSaed/Investigacion/blob/main/img-github/diagrama.png" width=750 height=450></td>
  </tr>
 </table>
 
 <br>

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

**Test en caliente:**
- Las consultas se realizaron de manera consecutiva.

**Test en frío:** 
- Las consultas se realizaron apagando el ordenador cada vez que se realizaba una consulta.

## Resultados

### Resultados Dataset Peliculas 

<table align="middle">
  <tr>
    <td><img src="https://github.com/DanielSaed/Investigacion/blob/main/img-github/pelicula.png" width=500 height=480></td>
    <td><img src="https://github.com/DanielSaed/Investigacion/blob/main/img-github/PeliculasFrio.png" width=500 height=480></td>
  </tr>
 </table>

### Resultados Dataset Ruta Aviones 

<table align="middle">
  <tr>
    <td><img src="https://github.com/DanielSaed/Investigacion/blob/main/img-github/Aviones.png" width=500 height=480></td>
    <td><img src="https://github.com/DanielSaed/Investigacion/blob/main/img-github/AvionesFrio.png" width=500 height=480></td>
  </tr>
 </table>

### Resultados Dataset Denue 

<table align="middle">
  <tr>
    <td><img src="https://github.com/DanielSaed/Investigacion/blob/main/img-github/Denue.png" width=500 height=480></td>
    <td><img src="https://github.com/DanielSaed/Investigacion/blob/main/img-github/DenueFrio.png" width=500 height=480></td>
  </tr>
 </table>

## Conclusion

Al usar bases de datos NoSQL que usan el mismo tipo de dato se elimina una variable que podría afectar a un análisis de los resultados. Entendiendo el hecho que un mejor rendimiento no significa que una base de datos es mejor o peor. Todas las bases de datos testeadas no tuvieron algún problema mayor en todos los procesos (instalación, configuración, subida de datos, consultas) solamente Couchbase tuvo algunas complicaciones menores que tuvieron impacto en el tiempo de desarrollo de esta investigación, sin embargo, una vez que se familiarizo con esta base de datos no se tuvo problema alguno.

La diferencia entre consultas de caliente y frio fueron significativas dependiendo la base de datos, CosmoDB fue el motor de base de datos que perdió más rendimiento comparándolo con su rendimiento en caliente, mientras que Couchbase fue el que menos rendimiento perdió. Couchbase necesito el uso de indexes personalizados para poder tener tiempos competitivos. 

En ocasiones esporádicas una consulta con más registros fue más rápida que una con menos registros, en consultas en frio este comportamiento se da por la inestabilidad de este tipo de consulta, es el caso de CosmoDB y Couchbase, sin embargo, en consultas en caliente solo MongoDB mostro ese comportamiento, esto es debido a la dificultad de la consulta.

El resultado que se intentó conseguir era encontrar cual motor de base de datos NoSQL era el más rápido en cada una de las condiciones, MongoDB fue el motor de base de datos con mejor rendimiento, además de encontrar fortalezas y debilidades de estos motores de base de datos comparándolos entre sí, Couchbase tiene más potencial del mostrado en esta investigación, sin embargo es complicado encontrar esa optimización que se desea, CosmoDB Cuenta con el respaldo de Azure-Microsoft por lo que es una fuerte opción si se está familiarizado con alguna tecnología de Microsoft. MongoDB es muy versátil y una de las mejores opciones del mercado.


