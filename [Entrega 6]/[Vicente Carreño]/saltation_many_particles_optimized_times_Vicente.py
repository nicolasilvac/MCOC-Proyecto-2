from matplotlib.pylab import *

Nparticulas = [1, 2, 4, 8, 12, 16, 20, 26, 32, 40, 50, 100]

tiempo_1_bloque1  =2.25099778175
tiempo_2_bloque1  =2.25199723244
tiempo_4_bloque1  =2.45400071144
tiempo_8_bloque1  =2.08600449562
tiempo_12_bloque1 =2.60699772835
tiempo_16_bloque1 =2.24699640274
tiempo_20_bloque1 =2.61300301552
tiempo_26_bloque1 =2.5819978714
tiempo_32_bloque1 =3.29800415039
tiempo_40_bloque1 =2.72000646591
tiempo_50_bloque1 =2.87700605392
tiempo_100_bloque1=3.52499866486

tiempo_1_bloque2= 3.94900155067
tiempo_2_bloque2=7.21000218391
tiempo_4_bloque2=14.0939991474
tiempo_8_bloque2=28.3529956341
tiempo_12_bloque2=47.9590029716
tiempo_16_bloque2=57.7090029716
tiempo_20_bloque2=78.8169972897
tiempo_26_bloque2=111.051000595
tiempo_32_bloque2=138.923995495
tiempo_40_bloque2=174.791992903
tiempo_50_bloque2=221.917994261
tiempo_100_bloque2=618.565001726

tiempo_1_Final= tiempo_1_bloque1 + tiempo_1_bloque2
tiempo_2_Final= tiempo_2_bloque1 + tiempo_2_bloque2
tiempo_4_Final= tiempo_4_bloque1 + tiempo_4_bloque2
tiempo_8_Final= tiempo_8_bloque1 + tiempo_8_bloque2
tiempo_12_Final=  tiempo_12_bloque1 + tiempo_12_bloque2
tiempo_16_Final=  tiempo_16_bloque1 + tiempo_16_bloque2
tiempo_20_Final=  tiempo_20_bloque1 + tiempo_20_bloque2
tiempo_26_Final=  tiempo_26_bloque1 + tiempo_26_bloque2
tiempo_32_Final=  tiempo_32_bloque1 + tiempo_32_bloque2
tiempo_40_Final=  tiempo_40_bloque1 + tiempo_40_bloque2
tiempo_50_Final=  tiempo_50_bloque1 + tiempo_50_bloque2
tiempo_100_Final= tiempo_100_bloque1  + tiempo_100_bloque2

Tiempos_bloque_1 = [tiempo_1_bloque1,tiempo_2_bloque1,tiempo_4_bloque1,tiempo_8_bloque1,tiempo_12_bloque1,tiempo_16_bloque1,tiempo_20_bloque1,tiempo_26_bloque1,tiempo_32_bloque1,tiempo_40_bloque1,tiempo_50_bloque1,tiempo_100_bloque1]
Tiempos_bloque_2 = [tiempo_1_bloque2,tiempo_2_bloque2,tiempo_4_bloque2,tiempo_8_bloque2,tiempo_12_bloque2,tiempo_16_bloque2,tiempo_20_bloque2,tiempo_26_bloque2,tiempo_32_bloque2,tiempo_40_bloque2,tiempo_50_bloque2,tiempo_100_bloque2]
Tiempos_Final = [tiempo_1_Final,tiempo_2_Final,tiempo_4_Final,tiempo_8_Final,tiempo_12_Final,tiempo_16_Final,tiempo_20_Final,tiempo_26_Final,tiempo_32_Final,tiempo_40_Final,tiempo_50_Final,tiempo_100_Final]

figure()
subplot(2,1,1)
plot(Nparticulas,Tiempos_bloque_1)
title("Grafico Tiempo Bloque 1 vs Numero de particulas",size=10)
ylabel("Tiempo [s]")
#xlabel("Numero de particulas")
yticks(Tiempos_bloque_1)

subplot(2,1,2)
plot(Nparticulas,Tiempos_bloque_2)
title("Grafico Tiempo Bloque 2 vs Numero de particulas",size=10)
ylabel("Tiempo [s]")
xlabel("Numero de particulas")
yticks(Tiempos_bloque_2)

figure()
plot(Nparticulas,Tiempos_Final)
title("Grafico Tiempo Final vs Numero de particulas",size=10)
ylabel("Tiempo [s]")
xlabel("Numero de particulas")
yticks(Tiempos_Final)


show()