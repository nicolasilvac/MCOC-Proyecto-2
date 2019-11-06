from matplotlib.pylab import *

Nparticulas = [1, 2, 4, 8, 12, 16, 20, 26, 32, 40, 50, 100]
 
tiempo_1_bloque1  = ( 3.03     +  2.25099778175    +   1.99600195885  + 6.81 	 ) / 4     
tiempo_2_bloque1  = ( 3.05     +  2.25199723244    +   2.26399874687  + 9.131	 ) / 4     
tiempo_4_bloque1  = ( 3.17     +  2.45400071144    +   2.28499531746  + 8.825	 ) / 4     
tiempo_8_bloque1  = ( 3.18     +  2.08600449562    +   2.52900147438  + 8.029	 ) / 4     
tiempo_12_bloque1 = ( 3.68     +  2.60699772835    +   2.28499531746  + 61.944   ) / 4  		
tiempo_16_bloque1 = ( 3.870    +  2.24699640274    +   2.23799729347  + 7.54	 ) / 4      
tiempo_20_bloque1 = ( 3.81     +  2.61300301552    +   2.51499915123  + 7.317	 ) / 4     
tiempo_26_bloque1 = ( 3.32     +  2.5819978714     +   2.40900087357  + 7.974	 ) / 4     
tiempo_32_bloque1 = ( 3.44     +  3.29800415039    +   2.63300204277  + 12.535   ) / 4  
tiempo_40_bloque1 = ( 3.74     +  2.72000646591    +   2.48399949074  + 7.403	 ) / 4     
tiempo_50_bloque1 = ( 4.01     +  2.87700605392    +   3.00600028038  + 7.509	 ) / 4     
tiempo_100_bloque1= ( 3.87     +  3.52499866486    +   3.46799635887  + 9.776	 ) / 4     
tiempo_1_bloque2  = ( 5.87     +  3.94900155067    +   4.40599799156  + 17.24	 ) / 4		
tiempo_2_bloque2  = ( 11.67    +  7.21000218391    +   8.6380007267   + 39.912   ) / 4	
tiempo_4_bloque2  = ( 23.79    +  14.0939991474    +   16.496004343   + 75.43    ) / 4		
tiempo_8_bloque2  = ( 49.37    +  28.3529956341    +   33.2389988899  + 133.303  ) / 4	
tiempo_12_bloque2 = ( 80.45    +  47.9590029716    +   53.0690031052  + 193.473  ) / 4	
tiempo_16_bloque2 = ( 114.19   +  57.7090029716    +   70.3759992123  + 263.906  ) / 4 
tiempo_20_bloque2 = ( 135.61   +  78.8169972897    +   89.7030003071  + 323.859  ) / 4 
tiempo_26_bloque2 = ( 171.43   +  111.051000595    +   120.274999619  + 443.852  ) / 4	
tiempo_32_bloque2 = ( 218.93   +  138.923995495    +   152.211996555  + 682.535  ) / 4	
tiempo_40_bloque2 = ( 287.79   +  174.791992903    +   196.208000183  + 682.059  ) / 4 	
tiempo_50_bloque2 = ( 381.16   +  221.917994261    +   260.228999853  + 899.217  ) / 4	
tiempo_100_bloque2= ( 869.08   +  618.565001726    +   628.411002636  + 2588.06  ) / 4	

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

Tiempos_bloque_1_ = [tiempo_1_bloque1,tiempo_32_bloque1,tiempo_40_bloque1,tiempo_50_bloque1,tiempo_100_bloque1]
Tiempos_bloque_2_ = [tiempo_1_bloque2,tiempo_8_bloque2,tiempo_16_bloque2,tiempo_26_bloque2,tiempo_32_bloque2,tiempo_40_bloque2,tiempo_50_bloque2,tiempo_100_bloque2]
Tiempos_Final_ = [tiempo_1_Final,tiempo_8_Final,tiempo_16_Final,tiempo_20_Final,tiempo_26_Final,tiempo_32_Final,tiempo_40_Final,tiempo_50_Final,tiempo_100_Final]

figure()
subplot(2,1,1)
plot(Nparticulas,Tiempos_bloque_1)
title("Grafico T Bloque 1 vs Numero de particulas",size=10)
ylabel("Tiempo [s]")
#xlabel("Numero de particulas")
#yticks(Tiempos_bloque_1_)

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
