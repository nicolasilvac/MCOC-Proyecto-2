from matplotlib.pylab import *
#Unidades base
_metro= 1
_kg= 1
_s=1
_mm= 10**-3*_m
_gr= 10**-3*_kg

vfx= 5*_m/_s # m/s
vfy= 0*_m/_s # m/s

x0=array([0,1],dtype=double) #posicion actual
v0=array([1,1],dtype=double) #velocidad actual

xi=zeros(2,dtype=double) #posicion siguiente
vi=zeros(2,dtype=double) #Velocidad siguiente
xim1=zeros(2,dtype=double)
vim1=zeros(2,dtype=double)

g=9.81*_m/_s**2
d=1*_mm
rho=2700*_kg/(_m**3)
Cd=0.47 #Para particula esferica
m= rho*pi*(d**3)*(4/3/8) #Masa de particula (grano de arena)
#Inicializar Euler en x0

dt=(10**-6)*_s 	#Paso de tiempo
tmax=20*_s #Tiempo max de simulacion
ti=0

w=array([0,-m*g])
vf=array([vfx,vfy])

Nt=int32(2*tmax/dt)
x_store=zeros((2,Nt))
v_store=zeros((2,Nt))
t_store=zeros((Nt))
#Metodo de euler
i=0
while ti<tmax:
	if i%100==0:
		print 'ti=',ti
	print 'xi=',xi
	print 'vi=',vi
	#Evaluar v. relativa
	vrel=vf-vi #vf=velocidad del flujo
	norm_vrel= vrel.norm()
	#Evaluar fuerzas sobre particulas
	fD= 0.5*Cd*norm_vrel*vrel #Fuerza drag
	Fi=W+fD
	#Evaluar aceleracion
	ai=Fi/m
	#Integrar
	xim1=xi+vi*dt+ai*(dt**2/2)
	vim1= vi + ai*dt
	#Avanzar al siguiente paso
	x_store[:,i]=xi
	v_store[:,i]=vi
	t_store[:]=ti
	ti+=dt
	i+=1
	xi=xim1
	vi=vim1
x_store.append(xi)
v_store.append(vi)
t_store.append(ti)
figure()
plot(x_store[0,:i],x_store[])























