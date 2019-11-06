from matplotlib.pylab import *

Nparticulas = [1, 2, 4, 8, 12, 16, 20, 26, 32, 40, 50, 100]

tiempo_1_bloque1  =3.03               #tiempo_1_bloque1  =3.03800106049
tiempo_2_bloque1  =3.05               #tiempo_2_bloque1  =3.05200624466
tiempo_4_bloque1  =3.17               #tiempo_4_bloque1  =3.17499661446
tiempo_8_bloque1  =3.18              #tiempo_8_bloque1  =3.1890001297
tiempo_12_bloque1 = 3.68                 #tiempo_12_bloque1 = 3.68500614166
tiempo_16_bloque1 =3.870               #tiempo_16_bloque1 =3.87099123001
tiempo_20_bloque1 = 3.81                 #tiempo_20_bloque1 = 3.81999659538
tiempo_26_bloque1 = 3.32                #tiempo_26_bloque1 = 3.32299971581
tiempo_32_bloque1 =3.44                #tiempo_32_bloque1 =3.44700098038
tiempo_40_bloque1 =3.74                #tiempo_40_bloque1 =3.74099683762
tiempo_50_bloque1 =4.01               #tiempo_50_bloque1 =4.0189909935
tiempo_100_bloque1=3.87                #tiempo_100_bloque1=3.87899708748                

tiempo_1_bloque2  = 5.87              #tiempo_1_bloque2= 5.87299776077
tiempo_2_bloque2  =11.67            #tiempo_2_bloque2=11.674993515
tiempo_4_bloque2  =23.79            #tiempo_4_bloque2=23.796002388
tiempo_8_bloque2  =49.37             #tiempo_8_bloque2=49.3769989014
tiempo_12_bloque2 =80.45            #tiempo_12_bloque2=80.4539945126
tiempo_16_bloque2 =114.19            #tiempo_16_bloque2=114.197008848
tiempo_20_bloque2 = 135.61              #tiempo_20_bloque2= 135.614002466
tiempo_26_bloque2 =171.43             #tiempo_26_bloque2=171.437000275
tiempo_32_bloque2 =218.93             #tiempo_32_bloque2=218.934997559
tiempo_40_bloque2 =287.79             #tiempo_40_bloque2=287.796002865
tiempo_50_bloque2 =381.16             #tiempo_50_bloque2=381.166008949
tiempo_100_bloque2=869.08             #tiempo_100_bloque2=869.083002329

tiempo_1_Final=   tiempo_1_bloque1 +    tiempo_1_bloque2
tiempo_2_Final=   tiempo_2_bloque1 +    tiempo_2_bloque2
tiempo_4_Final=   tiempo_4_bloque1 +    tiempo_4_bloque2
tiempo_8_Final=   tiempo_8_bloque1 +    tiempo_8_bloque2
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

Tiempos_bloque_1_ = [tiempo_1_bloque1,tiempo_8_bloque1,tiempo_16_bloque1,tiempo_20_bloque1,tiempo_26_bloque1,tiempo_32_bloque1,tiempo_40_bloque1,tiempo_50_bloque1,tiempo_100_bloque1]
Tiempos_bloque_2_ = [tiempo_1_bloque2,tiempo_8_bloque2,tiempo_16_bloque2,tiempo_26_bloque2,tiempo_32_bloque2,tiempo_40_bloque2,tiempo_50_bloque2,tiempo_100_bloque2]
Tiempos_Final_ = [tiempo_1_Final,tiempo_8_Final,tiempo_16_Final,tiempo_20_Final,tiempo_26_Final,tiempo_32_Final,tiempo_40_Final,tiempo_50_Final,tiempo_100_Final]

figure()
subplot(2,1,1)
plot(Nparticulas,Tiempos_bloque_1)
title("Grafico T Bloque 1 vs Numero de particulas",size=10)
ylabel("Tiempo [s]")
#xlabel("Numero de particulas")
yticks(Tiempos_bloque_1_)

subplot(2,1,2)
plot(Nparticulas,Tiempos_bloque_2)
title("Grafico T Bloque 2 vs Numero de particulas",size=10)
ylabel("Tiempo [s]")
xlabel("Numero de particulas")
yticks(Tiempos_bloque_2_)
savefig('Grafico Tiempos Bloques')

figure()
plot(Nparticulas,Tiempos_Final)
title("Grafico T Final vs Numero de particulas",size=10)
ylabel("Tiempo [s]")
xlabel("Numero de particulas")
yticks(Tiempos_Final_)

savefig('Grafico Tiempo Final')

show()
