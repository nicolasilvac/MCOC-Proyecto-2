#Entrega 3 MCOC-Proyecto-2
from matplotlib.pylab import *

#Unidades base

_m = 1. #metros
_kg = 1.
_s = 1.
_mm = 10.**-3*_m 
_gr = 10.**-3*_kg

vfx= 5.*_m/_s # m/s
vfy= 0.*_m/_s # m/s

x0 = array([0.,1.], dtype = double) #posicion actual
v0 = array([1.,1.], dtype = double) #velocidad actual

xi = x0 #posicion siguiente #vector tamano 2
vi = v0 #velocidad siguiente #vector tamano 2
xim1 = zeros(2.,dtype=double)
vim1 = zeros(2.,dtype=double)

g = 9.81*_m/_s**2
d = 1.*_mm
rho = 2700.*_kg/(_m**3)
Cd = 0.47 #Para particula esferica
m = rho*pi*(d**3)*(4./3./8.) #Masa de particula (grano de arena)
	#Inicializar Euler en x0
	
dt = (2e-6)*_s 	#Paso de tiempo
tmax = 0.1*_s #Tiempo max de simulacion
ti = 0.0*_s #Tiempo inicial

w = array([0,-m*g]) #vector peso
vf = array([vfx,vfy]) #matriz de  vfx filas y vfy columnas

Nt = int32(2*tmax/dt) #numeros de paso del tiempo, tiene que ser entero
x_store = zeros((2,Nt)) #guardar posiciones en cada tiempo 
v_store = zeros((2,Nt)) #guardar velocidades en cada timepo
t_store = zeros((Nt)) #solo un tiempo, arreglos con 0
#Metodo de euler
i=0
while ti<tmax:

	if i % 100 == 0:
		print 'ti=',ti ," |xi| = ", sqrt(dot(xi,xi))
	#print 'xi=',xi
	#print 'vi=',vi

	#Evaluar v. relativa
	vrel= vf-vi #vf=velocidad del flujo
	norm_vrel= sqrt(dot(vrel,vrel)) #norma de vrel

	#Evaluar fuerzas sobre particulas

	fD = 0.5 * Cd * norm_vrel * vrel #Fuerza drag
	Fi = w + fD
	#Hasta ahora lo que hay es la fuerza que hay en cada particula en cada tiempo discreto

	#Evaluar aceleracion
	ai = Fi / m

	#Integrar
	xim1 = xi + vi*dt + ai*(dt**2/2)
	vim1 = vi + ai*dt
	
	#Avanzar al siguiente paso
	x_store[:,i] = xi #se guarda el componente actual
	v_store[:,i] = vi
	t_store[:] = ti

	ti += dt
	i += 1
	xi = xim1
	vi = vim1

#guardar ultimo paso
x_store[:,i] = xi
v_store[:,i] = vi
t_store[i] = ti


print x_store

figure()
plot(x_store[0,:i],x_store[1,:i])
show()

