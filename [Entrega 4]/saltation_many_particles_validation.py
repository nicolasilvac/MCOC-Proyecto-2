from matplotlib.pylab import *
from scipy.integrate import odeint
import random

#Unidades base son SI (m, kg, s)
_m = 1.
_kg = 1.
_s = 1.
_mm = 1e-3*_m
_cm = 1e-2*_m
_gr = 1e-3*_kg

#Parametros basicos
g = 9.81*_m/_s**2
d = 1*_mm
rho_agua = 1000.*_kg/(_m**3)
rho_particula = 2650.*_kg/(_m**3)
Cd = 0.47 #para una particula
A = pi*(d/2)**2
V = (4./3.)*pi*(d/2)**3
m = rho_particula*V

#funcion para crear la particula
norm = lambda v: sqrt(dot(v,v))
def particula(z, t):
	xi = z[:2]
	vi = z[2:]
	vf = array([vfx, vfy])
	vrel = vf - vi
	fD = (0.5*Cd*rho_agua*A*norm(vrel))*vrel
	Fi = W + fD + fB

	#para choques de particulas
	k_penal = lambda v: 1000.*0.5*Cd*rho_agua*A*norm(v)/(1*_mm) 

	if xi[1] < 0:
		Fi[1] += -k_penal(v0)*xi[1]
	zp = zeros(4)
	zp[:2] = vi
	zp[2:] = Fi/m
	return zp

#condiciones 
vfx = 5.0*_m/_s
vfy = 0.*_m/_s

dt = 0.001*_s	#paso de tiempo
tmax = 2*_s		#tiempo maximo de simulacion
ti = 0.*_s		#tiempo actual

posicion = []#arreglo para guardar posiciones
velocidad = [] #arreglo para guardar velocidades

n = random.randint (1, 10)
print n
for i in range(n):
	vel = random.random()
	pos = random.random()
	x0 = array([0.,pos*_mm], dtype = double)
	v0 = array([1.,vel*2.], dtype = double)

	xi = x0 #actual posicion
	vi = v0 #actual velocidad
	xim1 = zeros(2, dtype = double) #posicion siguiente
	vim1 = zeros(2, dtype = double) #velocidad siguiente

	#fuerzas
	W = array([0, -m*g]) #fuerza weight
	fB = array([0, rho_agua*V*g]) #fuerza boyante

	#paso del tiempo
	t = arange(0, tmax, dt)
	Nt = len(t)

	z0 = zeros(4)
	z0[:2] = x0
	z0[2:] = v0
	z = odeint(particula, z0, t)
	posicion.append(z[:,:2])
	velocidad.append(z[:,2:])


plt.style.use('ggplot') #cambia el formato del grafico
figure()
for i in range(len(posicion)):	
	posicion_i=posicion[i]
	plot(posicion_i[:,0],posicion_i[:,1])
	ylim(0,8*_mm)
	plt.xlabel('POSICION HORIZONTAL (mm)') #nombre eje x
	plt.ylabel('POSICION VERTICAL (mm)') #nombre eje y
	plt.title('POSICION PARA MULTIPLES PARTICULAS') #titulo grafico 

figure()
for i in range(len(posicion)):
    posicion_i=posicion[i]
    velocidad_i=velocidad[i]
    subplot(2,1,1)
    plot(t,posicion_i[:,0])# label="x")
    plot(t,posicion_i[:,1])#, label="y")
    subplot(2,1,2)
    plot(t,velocidad_i[:,0])#, label="vx")
    plot(t,velocidad_i[:,1])#, label="vy")
show()

