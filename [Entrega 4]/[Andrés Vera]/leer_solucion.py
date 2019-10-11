from matplotlib.pylab import *

data_sol = load("solution.npz" )
t=data_sol["t"] 
z=data_sol["z"]
dt=data_sol["dt"]

Nparticulas = z.shape[1]/4

d = 0.15e-3

figure()
for i in range(Nparticulas):
	x = z[:,4*i]/d
	y = z[:,4*i+1]/d
	color=rand(3)
	plot(x,y,"--",color=color*0.9, alpha=0.3)
	plot(x[0::100],y[0::100],"o",color=color)

ylim([0,5])

#ideal si comparan con la mia directamente
show()