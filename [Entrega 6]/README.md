# Entrega 6
## Descripción

El objetivo de esta entrega es optimizar el tiempo de simulación de la [Entrega 4](https://github.com/nicolasilvac/MCOC-Proyecto-2/tree/master/%5BEntrega%204%5D)

## Metodología

El código se basa en iterar la posición en el plano XY de cada partícula, la cual depende de la velocidad del fluido, la fuerza resultante en la partícula, la cercanía con otras partículas y suelo, esta se comportará de una manera específica.

La optimización del código se basa en separar a las partículas que colisionan con las que no, ya que al colisionar, esto genera una ralentizacion de la implementación del código para las particulas aledañas en ese mismo tiempo.

Si bien los gráficos de trayectoria de las partículas son similares a la Entrega 4, los tiempos de simulación son menores a una implementación sin optimizar.

## Rendimiento en General
Se hizo un promedio del tiempo que la simulación se implementó para los 4 integrantes del grupo para varios numeros de particulas:
### Tiempos de simulación

- Para 1 partículas el tiempo es de = 
- Para 2 partículas el tiempo es de = 
- Para 4 partículas el tiempo es de = 
- Para 8 partículas el tiempo es de = 
- Para 12 partículas el tiempo es de = 
- Para 16 partículas el tiempo es de = 
- Para 20 partículas el tiempo es de = 
- Para 26 partículas el tiempo es de = 
- Para 32 partículas el tiempo es de = 
- Para 40 partículas el tiempo es de = 
- Para 50 partículas el tiempo es de = 
- Para 100 partículas el tiempo es de = 

A continuación, se muestran en los gráficos tiempo vs numero de particulas, los tiempos promedios de los 4 integrantes del grupo, en primera ocasión se muestran los gráficos de:
- Bloque 1: Particulas que no colisionan
- Bloque 2: Particulas que colisionan
![](link)

Y en segunda ocasión se muestra el gráfico tiempo vs numero de particulas del total del tiempo de todas las particulas.

![](link)

El gráfico al que se pudo llegar para la Entrega 4 es el siguiente:

![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%204%5D/%5BGr%C3%A1ficos%5D/tiempo_simulacion_segun_particulas_grupo.png)

Comparando los gráficos de tiempos finales de la Entrega 4 y la actual, se puede concluir que la separación de particulas si contribuye a una mejora en el desempeño del código.

## Gráficos de Trayectorias de Particulas

- Para 1 partículas: 
![](link)
- Para 2 partículas: 
![](link)
- Para 4 partículas:
![](link)
- Para 8 partículas:
![](link)
- Para 12 partículas: 
![](link)
- Para 16 partículas:
![](link)
- Para 20 partículas:
![](link)
- Para 26 partículas: 
![](link)
- Para 32 partículas:
![](link)
- Para 40 partículas: 
![](link)
- Para 50 partículas: 
![](link)
- Para 100 partículas:
![](link)
