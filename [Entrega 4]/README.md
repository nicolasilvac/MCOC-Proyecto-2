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

Para 2 partículas:
Para 5 partículas:
Para 10 partículas:
Para 20 partículas:







