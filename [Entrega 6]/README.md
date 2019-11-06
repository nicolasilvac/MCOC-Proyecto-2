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

#### Bloque 1 (Partículas que no colisionan) [s]
- Para 1 partículas el tiempo es de = 3.52
- Para 2 partículas el tiempo es de = 4.17
- Para 4 partículas el tiempo es de = 4.18
- Para 8 partículas el tiempo es de = 3.95
- Para 12 partículas el tiempo es de = 17.62
- Para 16 partículas el tiempo es de = 3.97
- Para 20 partículas el tiempo es de = 4.06
- Para 26 partículas el tiempo es de = 4.07
- Para 32 partículas el tiempo es de = 5.47
- Para 40 partículas el tiempo es de = 4.08
- Para 50 partículas el tiempo es de = 4.35
- Para 100 partículas el tiempo es de = 5.15

#### Bloque 2 (Partículas que si colisionan) [s]
- Para 1 partículas el tiempo es de = 7.86
- Para 2 partículas el tiempo es de = 16.85
- Para 4 partículas el tiempo es de = 32.45
- Para 8 partículas el tiempo es de = 61.06
- Para 12 partículas el tiempo es de = 93.73
- Para 16 partículas el tiempo es de = 126.54
- Para 20 partículas el tiempo es de = 156.99
- Para 26 partículas el tiempo es de = 211.65
- Para 32 partículas el tiempo es de = 298.15
- Para 40 partículas el tiempo es de = 335.21
- Para 50 partículas el tiempo es de = 440.63
- Para 100 partículas el tiempo es de = 1176.0

#### Tiempo Final [s]

- Para 1 partículas el tiempo es de = 11.38
- Para 2 partículas el tiempo es de = 21.03
- Para 4 partículas el tiempo es de = 36.63
- Para 8 partículas el tiempo es de = 65.02
- Para 12 partículas el tiempo es de = 111.36
- Para 16 partículas el tiempo es de = 130.51
- Para 20 partículas el tiempo es de = 161.06
- Para 26 partículas el tiempo es de = 215.72
- Para 32 partículas el tiempo es de = 303.62
- Para 40 partículas el tiempo es de = 339.29
- Para 50 partículas el tiempo es de = 444.98
- Para 100 partículas el tiempo es de = 1181.185


A continuación, se muestran en los gráficos tiempo vs numero de particulas, los tiempos promedios de los 4 integrantes del grupo, en primera ocasión se muestran los gráficos de:
- Bloque 1: Particulas que no colisionan
- Bloque 2: Particulas que colisionan
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/Gr%C3%A1ficos/Grafico%20Tiempos%20Bloques.png)

Y en segunda ocasión se muestra el gráfico tiempo vs numero de particulas del total del tiempo de todas las particulas.

![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/Gr%C3%A1ficos/Grafico%20Tiempo%20Final.png)

El gráfico al que se pudo llegar para la Entrega 4 es el siguiente:

![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%204%5D/%5BGr%C3%A1ficos%5D/tiempo_simulacion_segun_particulas_grupo.png)

Comparando los gráficos de tiempos finales de la Entrega 4 y la actual, se puede concluir que la separación de particulas si contribuye a una mejora en el desempeño del código.

## Gráficos de Trayectorias de Particulas

- Para 1 partículas: 
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/Gr%C3%A1ficos/Grafico%201%20particulas.png)
- Para 2 partículas: 
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/Gr%C3%A1ficos/Grafico%202%20particulas.png)
- Para 4 partículas:
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/Gr%C3%A1ficos/Grafico%204%20particulas.png)
- Para 8 partículas:
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/Gr%C3%A1ficos/Grafico%208%20particulas.png)
- Para 12 partículas: 
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/Gr%C3%A1ficos/Grafico%2012%20particulas.png)
- Para 16 partículas:
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/Gr%C3%A1ficos/Grafico%2016%20particulas.png)
- Para 20 partículas:
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/Gr%C3%A1ficos/Grafico%2020%20particulas.png)
- Para 26 partículas: 
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/Gr%C3%A1ficos/Grafico%2026%20particulas.png)
- Para 32 partículas:
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/Gr%C3%A1ficos/Grafico%2032%20particulas.png)
- Para 40 partículas: 
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/Gr%C3%A1ficos/Grafico%2040%20particulas.png)
- Para 50 partículas: 
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/Gr%C3%A1ficos/Grafico%2050%20particulas.png)
- Para 100 partículas:
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/Gr%C3%A1ficos/Grafico%20100%20particulas.png)
