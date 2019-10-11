## Rendimiento del Programa
### Especificaciones del Computador
- Marca: Sony
- Procesador: Intel Core i5-2430M de 2.40GHz
- RAM: 4 GB
- Tarjeta de Video: NVIDIA GeoForce 410M
- Sistema Operativo: Windows 10 Hombre, 64 bits

### Tiempos de simulación

- Para 2 partículas = 0.34s
- Para 5 partículas = 1.73s
- Para 10 partículas = 16.05s
- Para 20 partículas = 200.94s

![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%204%5D/%5BNicol%C3%A1s%20Silva%5D/tiempo_simulacion_segun_particulas.png)

De este gráfico se puede notar que para un bajo número de partículas el tiempo de simulación es bajo, sin embargo, al aumentarlas, el tiempo aumenta de manera exponencial. Esto se puede deber a los ciclos que posee el código, ya que estos se encuentran dentro de otros ciclos, entonces al subir el rango del bucle el número de iteraciones aumenta notoriamente.

Para mejorar los poder tener un mejor desempeño en cuanto a la disminución del tiempo de simulación se puede aumentar, por ejemplo el paso del tiempo, en el caso de nuestro grupo el paso del tiempo es de 0.001s, y el tiempo máximo es de 2 segundos, por lo que el número de iteraciones para el paso del tiempo es de 2000, entonces, si, por ejemplo se aumentara el paso de tiempo a 0.005 el número de iteraciones sería de 400, es decir el 25% del número de iteraciones anteriores. 

Este ejemplo se verifica al implementarlo en el código para 10 partículas, en un principio es el siguiente:
<pre>
#transcurso del tiempo
dt = 0.001*_s	#paso de tiempo
tmax = 0.5*_s		#tiempo maximo de simulacion
ti = 0. * _s 	#tiempo actual
</pre>
Con un tiempo de simulación de 16.05s

Por otro lado, se implementa mismo código pero con un paso de tiempo de 0.005 s, como se puede ver a continuación:
<pre>
#transcurso del tiempo
dt = 0.005*_s	#paso de tiempo
tmax = 0.5*_s		#tiempo maximo de simulacion
ti = 0. * _s 	#tiempo actual
</pre>
Con un tiempo de simulación de 14.91s
