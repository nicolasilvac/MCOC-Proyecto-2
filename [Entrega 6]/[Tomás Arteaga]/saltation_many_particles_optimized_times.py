from matplotlib.pylab import *



Nparticulas = [1, 2, 4, 8, 12, 16, 20, 26, 32, 40, 50, 100]



tiempo_1_bloque1  = 1.99600195885

tiempo_2_bloque1  =2.26399874687

tiempo_4_bloque1  =2.28499531746

tiempo_8_bloque1  = 2.52900147438

tiempo_12_bloque1 =2.23799729347

tiempo_16_bloque1 =2.51499915123

tiempo_20_bloque1 =2.40900087357

tiempo_26_bloque1 =2.61400079727

tiempo_32_bloque1 = 2.63300204277

tiempo_40_bloque1 =2.48399949074

tiempo_50_bloque1 =3.00600028038

tiempo_100_bloque1=3.46799635887



tiempo_1_bloque2= 4.40599799156

tiempo_2_bloque2=8.6380007267

tiempo_4_bloque2=16.496004343

tiempo_8_bloque2=33.2389988899

tiempo_12_bloque2=53.0690031052

tiempo_16_bloque2=70.3759992123

tiempo_20_bloque2=89.7030003071

tiempo_26_bloque2=120.274999619

tiempo_32_bloque2=152.211996555

tiempo_40_bloque2=196.208000183

tiempo_50_bloque2=260.228999853

tiempo_100_bloque2=628.411002636




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
