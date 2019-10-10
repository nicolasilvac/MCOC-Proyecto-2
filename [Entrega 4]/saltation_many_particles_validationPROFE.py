
from matplotlib.pylab import * 

#Unidades base son SI (m, kg, s)
_m = 1.
_kg = 1.
_s = 1.
_mm = 1e-3*_m
_cm = 1e-2*_m
_gr = 1e-3*_kg
_in = 2.54*_cm

g = 9.81*_m/_s**2
d = 0.56*_mm

rho_agua = 1000. *_kg/(_m**3)
rho_particula = 2650. *_kg/(_m**3)


dt = 0.001*_s	#paso de tiempo
tmax =0.01#0.1 * _s   #tiempo maximo de simulacion
ti = 0. * _s #tiempo actual

Nparticulas = 2

x0 = 10*d*rand(Nparticulas)
y0 = 3*d*rand(Nparticulas)

vx0 = rand(Nparticulas)/2
vy0 = rand(Nparticulas)/2

A = pi*(d/2)**2
V = (4./3.)*pi*(d/2)**3
m = rho_particula*V

W = array([0, -m*g])

t = arange(0, tmax, dt)
Nt = len(t)

norm = 1000*0.5*Cd*rho_agua*A*norm(vfx)/(1*_mm)

Cd = 0.47 #para una particula
Cm = 0.5
CL = 0.2
Rp = 73. #250
R = (rho_particula/rho_agua -1)
alpha = 1/(1 + R + Cm)

ihat = array([1,0])
jhat = array([0,1])

#TODO ESTO LO BORRA EL PROFE vff = array([vfx, vfy])
#TODO ESTO LO BORRA EL PROFE  def velocity_field(x):
#TODO ESTO LO BORRA EL PROFE 	return vff
def velocity_field(x):
	z = x[1] / d
	if z > 1. /30:
		uf = log(30.*z)/0,41
	else:
		uf = 0 
def particula(z,t):
	zp = zeros(4*Nparticulas)

	for i in range(Nparticulas):
		di = d
		xi = z[4*i:(4*i+2)]
		vi = z[4*i+2:(4*i+4)]
		vf = velocity_field(xi)
		vf_top = norm(velocity_field(xi + di/2*jhat))
		vf_bot = norm(velocity_field(xi - di/2*jhat))
		vrel = vf - vi
		fD = (0.5*C¨*alpha*rho_agua*norm(vrel)*A)vrel
		fL = (0.5*CL*alpha*rho_agua*(vf_top - vf_bot)*A)*jhat

		Fi = W + fD + fL

		if xi[1] <0:
			Fi[1] += -k_penal*xi[1]

		zp[4*i:(4*i+2)] = vi
		zp[4*i+2:(4*i+4)] = Fi/m

	for i in range(Nparticulas):
		xi = z[4*i:(4*i+2)]
		for i in range(Nparticulas):
			if i > j:
				xj = z[4*j:(4*j+2)]
				rij = xj - xi
				if norm(rij) < d:
					delta = d - norm(rij)
					nij = rij/norm(rij)
					Fj = K_penal*nij
					Fi = -k_penal*nij
					zp[4*i+2:(4*i+4)] += Fi/m
					zp[4*j+2:(4*j+4)] += Fj/m

	return zp

from scipy.integrate import odeint
z0 = zeros(4*Nparticulas)
z0[0:: 4] = x0
z0[1:: 4] = y0
z0[2:: 4] = vx0
z0[3:: 4] = vy0

print "Integrando"
z = odeint(particula, z0, t)
print "fin"
fig = figure()

ax= gca()
for i in range(Nparticulas):
	xi = z[:, 4*i]
	yi = z[:, 4*i+1]
	col = rand(3)
	plot(xi,yi,color=col)
	for x,y in zip(xi, yi):
		ax.add artist(Circle(xy=(x,y),
						radius=d/2,color=col,alpha= 0.7)




# ylimt([0.10*_mm])

# figure() 
# subplot(2,2,1)
# plot(t,x[:,0],label= "x")
# plot(t,x[:,1],label= "y")
# subplot(2,1,2)
# plot(t,v[:,0],label = "vx")
# plot(t,v[:,1],label = "vy")

#axis("equal")

show()