# Entrega 4
## Descripción

El objetivo de esta entrega es poder simular el transporte de sedimentos de fondo en base a un método lagrangiano, en esta oportunidad se simuló para 2, 5, 10 y 20 partículas. Para ello se consideraron fuerzas del peso propio de la partícula, drag y liftting, para las cuales se consideraron los siguientes parámetros:

#### Físicos y Geométricos
- Densidad de la partícula de sedimento 2650 kg/m3 (suelo mineral)
- Densidad del agua 1000 kg/m3
- Diámetro de la partícula de sedimento de 1 mm

#### La posición y velocidad inicial se utilizó el método siguiente:
<pre>
  x0 = 100*d*rand(Nparticulas)
  y0 = 30*d*rand(Nparticulas) + d
  vx0 = rand(Nparticulas)/2
  vy0 = rand(Nparticulas)/2
</pre>

  
#### Los coeficientes para utilizar las fórmulas de fuerzas
- Constante de drag = 0.47 (partícula esférica)
- Constante de lifting = 0.2
- u_estrella = 0.14

Además, se consideró un tiempo total de 2 segundos para el movimiento de las partículas.
## Metodología

El código se basa en iterar la posición en el plano XY de cada partícula, la cual depende de la velocidad del fluido, la fuerza resultante en la partícula, la cercanía con otras partículas y suelo, esta se comportará de una manera específica.

## Resultados

### Para 2 partículas:
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%204%5D/%5BGr%C3%A1ficos%5D/simulacion_2.png)
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%204%5D/%5BGr%C3%A1ficos%5D/trayectoria_2.png)
### Para 5 partículas:
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%204%5D/%5BGr%C3%A1ficos%5D/simulacion_5.png)
#### Acercamiento:
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%204%5D/%5BGr%C3%A1ficos%5D/simulacion_5_zoom.png)
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%204%5D/%5BGr%C3%A1ficos%5D/trayectoria_5.png)
### Para 10 partículas:
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%204%5D/%5BGr%C3%A1ficos%5D/simulacion_10.png)
#### Acercamiento:
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%204%5D/%5BGr%C3%A1ficos%5D/simulacion_10_zoom.png)
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%204%5D/%5BGr%C3%A1ficos%5D/trayectoria_10.png)
### Para 20 partículas:
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%204%5D/%5BGr%C3%A1ficos%5D/simulacion_20.png)
#### Acercamiento:
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%204%5D/%5BGr%C3%A1ficos%5D/simulacion_20_zoom.png)
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%204%5D/%5BGr%C3%A1ficos%5D/trayectoria_20.png)


## Rendimiento en General
Se hizo un promedio del tiempo que la simulación se implementó para los 4 integrantes del grupo para 2, 5, 10 y 20 partículas.

### Tiempos de simulación
- Para 2 partículas = 0.29 segundos
- Para 5 partículas = 1.43 segundos
- Para 10 partículas = 11.60 segundos
- Para 20 partículas = 164.36 segundos
![](grafico)
El cual se puede ver en la figura anterior cómo el gráfico de particulas vs tiempo se acerca a una curva exponencial, es decir, para cuando el número de partículas crece en rangos muy altos, el tiempo de simulación crece considerablemente en relación a cuando el número de partículas crecen en rangos pequeños.




