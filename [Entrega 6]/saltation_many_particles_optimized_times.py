from matplotlib.pylab import *

Nparticulas = [1, 2, 4, 8, 12, 16, 20, 26, 32, 40, 50, 100]

tiempo_1_bloque1  =
tiempo_2_bloque1  =
tiempo_4_bloque1  =
tiempo_8_bloque1  =
tiempo_12_bloque1 =
tiempo_16_bloque1 =
tiempo_20_bloque1 =
tiempo_26_bloque1 =
tiempo_32_bloque1 =
tiempo_40_bloque1 =
tiempo_50_bloque1 =
tiempo_100_bloque1=

tiempo_1_bloque2= 
tiempo_2_bloque2=
tiempo_4_bloque2=
tiempo_8_bloque2=
tiempo_12_bloque2=
tiempo_16_bloque2=
tiempo_20_bloque2=
tiempo_26_bloque2=
tiempo_32_bloque2=
tiempo_40_bloque2=
tiempo_50_bloque2=
tiempo_100_bloque2=

tiempo_1_Final= tiempo_1_bloque1 + tiempo_2_bloque1
tiempo_2_Final= tiempo_1_bloque2 + tiempo_2_bloque2
tiempo_4_Final= tiempo_1_bloque4 + tiempo_2_bloque4
tiempo_8_Final= tiempo_1_bloque8 + tiempo_2_bloque8
tiempo_12_Final=  tiempo_1_bloque12 + tiempo_2_bloque12
tiempo_16_Final=  tiempo_1_bloque16 + tiempo_2_bloque16
tiempo_20_Final=  tiempo_1_bloque20 + tiempo_2_bloque20
tiempo_26_Final=  tiempo_1_bloque26 + tiempo_2_bloque26
tiempo_32_Final=  tiempo_1_bloque32 + tiempo_2_bloque32
tiempo_40_Final=  tiempo_1_bloque40 + tiempo_2_bloque40
tiempo_50_Final=  tiempo_1_bloque50 + tiempo_2_bloque50
tiempo_100_Final= tiempo_1_bloque100  + tiempo_2_bloque100

Tiempos_bloque_1 = [tiempo_1_bloque1,tiempo_2_bloque1,tiempo_4_bloque1,tiempo_8_bloque1,tiempo_12_bloque1,tiempo_16_bloque1,tiempo_20_bloque1,tiempo_26_bloque1,tiempo_32_bloque1,tiempo_40_bloque1,tiempo_50_bloque1,tiempo_100_bloque1]
Tiempos_bloque_2 = [tiempo_1_bloque2,tiempo_2_bloque2,tiempo_4_bloque2,tiempo_8_bloque2,tiempo_12_bloque2,tiempo_16_bloque2,tiempo_20_bloque2,tiempo_26_bloque2,tiempo_32_bloque2,tiempo_40_bloque2,tiempo_50_bloque2,tiempo_100_bloque2]
Tiempos_Final = [tiempo_1_Final,tiempo_2_Final,tiempo_4_Final,tiempo_8_Final,tiempo_12_Final,tiempo_16_Final,tiempo_20_Final,tiempo_26_Final,tiempo_32_Final,tiempo_40_Final,tiempo_50_Final,tiempo_100_Final]

figure()
subplot(2,1,1)
plot(Nparticulas,Tiempos_bloque_1)
title("Grafico T Bloque 1 vs Numero de particulas",size=10)
ylabel("Tiempo [s]")
#xlabel("Numero de particulas")
yticks(Tiempos_bloque_1)

subplot(2,1,2)
plot(Nparticulas,Tiempos_bloque_2)
title("Grafico T Bloque 2 vs Numero de particulas",size=10)
ylabel("Tiempo [s]")
xlabel("Numero de particulas")
yticks(Tiempos_bloque_2)

figure()
plot(Nparticulas,Tiempos_Final)
title("Grafico T Final vs Numero de particulas",size=10)
ylabel("Tiempo [s]")
xlabel("Numero de particulas")
yticks(Tiempos_Final)


show()