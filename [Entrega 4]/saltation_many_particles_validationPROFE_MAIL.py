from scipy.integrate import odeint
from matplotlib.pylab import * 

#unidades base SI (m, kg, s)
_m = 1.
_kg = 1.
_s = 1.
_mm = 1e-3 *_m
_cm = 1e-2 *_m
_gr = 1e-3 *_kg
_in = 2.54 *_cm

#parametros fisicos
g = 9.81* _m/_s**2
d = 0.15* _cm
rho_agua = 1000. *_kg/(_m**3)		#densidad del agua
rho_particula = 2650. *_kg/(_m**3)	#densidad de las particulas

#condiciones iniciales
data = load("initial_condition.npz")
x0 = data["x0"]
y0 = data["y0"]
vx0 = data["vx0"]
vy0 = data["vy0"]
Nparticulas = data["Nparticulas"]
print "El numero de particulas en simulacion es = ", Nparticulas

#recursos para el transcurso de la simulacion
dt = 0.0001 *_s				#paso de tiempo
tmax = 1 *_s			  	#tiempo maximo de simulacion
ti = 0. * _s 				#tiempo actual
t = arange(0, tmax, dt)
Nt = len(t)

#parametros geometricos y masa
A = pi*(d/2)**2
V = (4./3.)*pi*(d/2)**3
m = rho_particula*V

#coeficientes para las particulas
Cd = 0.47 	#para una particula
Cm = 0.5	#masa adicional
CL = 0.2	#coeficiente de lift
Rp = 73. 	
R = (rho_particula/rho_agua - 1)
alpha = 1/(1 + R + Cm)				

#velocidad y shear stress del fluido
ustar = 0.14 # (m/s) 0.14 - 0.23 usestrella en formula
tau_star = 0.067	#tau star (shear stress)
tau_cr = 0.22*Rp**(-0.6) + 0.06*10**(-7*Rp**(-0.6))	#tau critico
ustar = sqrt(tau_star*g*Rp*d)
#print "tau_star = ", tau_star
#print "tau_cr = ", tau_cr
#print "tau_star/tau_cr = ", tau_star/tau_cr
#print "ustar = ", ustar


#directores y norma
ihat = array([1,0])		#itongo
jhat = array([0,1])		#jotatongo
norm = lambda v: sqrt(dot(v,v))

#perfil de velocidad logaritmica
def velocity_field(x):
	z = x[1] / d
	if z > 1/30:
		uf = ustar*log(30.*z)/0.41
		uf = uf * (uf > 0)
	else:
		uf = 0
	return array([uf,0])	#retorna un arreglo con las velocidades para cada particula 


vfx= velocity_field([0, 10*d])[0] 					#arreglo de las velocidades para cada particula
k_penal = 0.5*Cd*rho_agua*A*norm(vfx)**2/(d/20)		#lo que penaliza por choques entre particulas

#movimiento de la particula
def particula(z,t):
	zp = zeros(4*Nparticulas)
	for i in range(Nparticulas):
		di = d
		xi = z[4*i:(4*i+2)]
		vi = z[4*i+2:(4*i+4)]
		vf = velocity_field(xi)
		vf_top = norm(velocity_field(xi + (di/2)*jhat))
		vf_bot = norm(velocity_field(xi - (di/2)*jhat))
		vrel = vf - vi
		fD = (0.5*Cd*alpha*rho_agua*norm(vrel)*A)*vrel
		fL = (0.5*CL*alpha*rho_agua*(vf_top**2 - vf_bot**2)*A)*jhat
		fW = array([0, -m*g])
		Fi = fW + fD + fL

		if xi[1] < 0:	#la particula no puede estar mas abajo que el piso (altura 0)
			Fi[1] += -k_penal*xi[1]	#al estar por debajo la devuelve para arriba


		zp[4*i: (4*i+2)] = vi
		zp[4*i+2:(4*i+4)] = Fi/m

		for i in range(Nparticulas):
			xi = z[4*i:4*i+2]
			for j in range(Nparticulas):
				if i > j:
					xj = z[4*j:4*j+2]
					rij = xj - xi
					if norm(rij) < d:
						delta = d - norm(rij)
						nij = rij/norm(rij)
						Fj = k_penal*delta*nij
						Fi = -Fj
						zp[4*i+2:4*i+4] += Fi/m
						zp[4*j+2:4*j+4] += Fj/m

	return zp


z0 = zeros(4*Nparticulas)
z0[0::4] = x0
z0[1::4] = y0
z0[2::4] = vx0
z0[3::4] = vy0

print "Integrando"
z = odeint(particula, z0, t)
print "Fin"

#codigo para ploteo
fig = figure()
ax= gca()
for i in range(Nparticulas):
	xi = z[:, 4*i]
	yi = z[:, 4*i + 1]
	col = rand(3)
	plot(xi,yi,color=col)
	for x,y in zip(xi, yi):
		ax.add_artist(Circle(xy=(x,y),radius=d/2,color=col,alpha= 0.7))
ax.axhline(0,color="k",linestyle="--")
axis("equal")
show()