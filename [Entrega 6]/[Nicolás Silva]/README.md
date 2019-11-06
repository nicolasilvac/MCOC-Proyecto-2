## Rendimiento del Programa 
### Especificaciones del Computador
- Marca: Sony
- Procesador: Intel Core i5-2430M de 2.40GHz
- RAM: 4 GB
- Tarjeta de Video: NVIDIA GeoForce 410M
- Sistema Operativo: Windows 10 Home, 64 bits
- Año: 2015

### Tiempos de simulación

#### Bloque 1 (Partículas que no colisionan)
- Para 1 partículas el tiempo es de = 3.03 
- Para 2 partículas el tiempo es de = 3.05 
- Para 4 partículas el tiempo es de = 3.17 
- Para 8 partículas el tiempo es de = 3.18 
- Para 12 partículas el tiempo es de = 3.68
- Para 16 partículas el tiempo es de = 3.870
- Para 20 partículas el tiempo es de = 3.81
- Para 26 partículas el tiempo es de = 3.32
- Para 32 partículas el tiempo es de = 3.44 
- Para 40 partículas el tiempo es de = 3.74 
- Para 50 partículas el tiempo es de = 4.01 
- Para 100 partículas el tiempo es de = 3.87 

#### Bloque 2 (Partículas que si colisionan)
- Para 1 partículas el tiempo es de = 5.87   
- Para 2 partículas el tiempo es de = 11.67   
- Para 4 partículas el tiempo es de = 23.79   
- Para 8 partículas el tiempo es de = 49.37   
- Para 12 partículas el tiempo es de = 80.45   
- Para 16 partículas el tiempo es de = 114.19  
- Para 20 partículas el tiempo es de = 135.61 
- Para 26 partículas el tiempo es de = 171.43  
- Para 32 partículas el tiempo es de = 218.93  
- Para 40 partículas el tiempo es de = 287.79  
- Para 50 partículas el tiempo es de = 381.16  
- Para 100 partículas el tiempo es de = 869.08 

#### Tiempo Final

- Para 1 partículas el tiempo es de = 8.9
- Para 2 partículas el tiempo es de = 14.72
- Para 4 partículas el tiempo es de = 26.96
- Para 8 partículas el tiempo es de = 52.55
- Para 12 partículas el tiempo es de = 84.13
- Para 16 partículas el tiempo es de = 118.06
- Para 20 partículas el tiempo es de = 139.42
- Para 26 partículas el tiempo es de = 174.75
- Para 32 partículas el tiempo es de = 222.37
- Para 40 partículas el tiempo es de = 291.53
- Para 50 partículas el tiempo es de = 385.17
- Para 100 partículas el tiempo es de = 872.95

## Gráficos Tiempo vs Número de Partículas

![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/%5BNicol%C3%A1s%20Silva%5D/Gr%C3%A1ficos/Grafico%20Tiempos%20Bloques.png)
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/%5BNicol%C3%A1s%20Silva%5D/Gr%C3%A1ficos/Grafico%20Tiempo%20Final.png)

De estos gráficos se puede observar que el bloque 1, donde las partículas no colisionan, en general, es constante en función del número de partículas, por otro lado, el bloque 2, en donde las partículas sí colisionan, mientras más partículas hay, el tiempo es mayor, esto es debido a que la implementación del código debe recorrer un mayor número de iteraciones porque la partícula tiene trayectorias no homogeneas. Entonces el tiempo final depende significativamente del bloque 2, el cual es lineal, a simple vista, con el número de partículas.

## Gráficos de Trayectorias de Particulas
Alguno de los gráficos de las trayectoria de las partículas resultantes de las simulaciones fueron los siguientes:

- Para 2 partículas: 
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/Gr%C3%A1ficos/Grafico%202%20particulas.png)
- Para 8 partículas:
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/Gr%C3%A1ficos/Grafico%208%20particulas.png)
- Para 12 partículas: 
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/Gr%C3%A1ficos/Grafico%2012%20particulas.png)
- Para 20 partículas:
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/Gr%C3%A1ficos/Grafico%2020%20particulas.png)
- Para 32 partículas:
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/Gr%C3%A1ficos/Grafico%2032%20particulas.png)
- Para 50 partículas: 
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/Gr%C3%A1ficos/Grafico%2050%20particulas.png)
- Para 100 partículas:
![](https://github.com/nicolasilvac/MCOC-Proyecto-2/blob/master/%5BEntrega%206%5D/Gr%C3%A1ficos/Grafico%20100%20particulas.png)

