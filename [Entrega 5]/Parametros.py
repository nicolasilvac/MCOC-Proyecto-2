from matplotlib.pylab import *


#Unidades base son SI (m, kg, s)
_m = 1.
_kg = 1.
_s = 1.
_mm = 1e-3*_m
_cm = 1e-2*_m
_gr = 1e-3*_kg
_in = 2.54*_cm



#parametros fisicos
g = 9.81*_m/_s**2
rho_agua = 1000.*_kg/(_m**3)		# Densidad del agua
rho_particula = 2650.*_kg/(_m**3)	# Densidad de las particulillas

#transcurso del tiempo
dt = 0.0001*_s    	# paso de tiempo 
tmax = 2*_s      # tiempo maximo de simulacion

#parametros geometricos y peso
d = 0.15*_mm
A = pi*(d/2)**2 		#Area Particula
V = (4./3.)*pi*(d/2)**3 #Volumen Particula
m = rho_particula*V 	#Masa particula

#coeficientes para formula
Cd = 0.47    #Coeficiente de arrastre
Cm = 0.5	#Masa adicional
CL = 0.2	#Coeficiente de lift
Rp = 73.  
R = (rho_particula/rho_agua - 1)  
ustar = 0.14	#  (m/s)  0.14 - 0.23 usestrella
alpha = 1/(1 + R + Cm)			
tau_star = 0.067   # Tau star (Shear stress)




Nparticulas = 20	#Numero de particulas

#Directores
ihat = array([1,0])			# itongo
jhat = array([0,1])			# jotatongo
norm=lambda v: sqrt(dot(v,v))

tau_cr = 0.22*Rp**(-0.6)+0.06*10**(-7*Rp**(-0.6))   # tau critico
ustar = sqrt(tau_star * g * Rp * d)		# uestrella de verdad ahora si final final ok para siempre

print "tau_star = ", tau_star
print "tau_cr = ", tau_cr
print "tau_star/tau_cr = ", tau_star/tau_cr
print "ustar = ", ustar

# formulillas que no estoy usando
# tau_ratio = 2
# Rep = ws*d/nu
# Rp_computed = (R*g*d**3)/nu 
# tau = ustar**2 / (g * Rp * d)


# ley de la pared.... 
# wall law.... the wall.... the law of pink floyd
def velocity_field(x):
	z = x[1] / d
	# z = x[1] 
	if z > 1/30.:
		uf = ustar*log(30.*z)/0.41
		uf = uf * (uf > 0)
	else:
		uf = 0

	return array([uf,0])

# estimar k_penal.... 
vfx = velocity_field([0, 10*d])[0]
A = pi*(d/2)**2
k_penal = 0.5*Cd*rho_agua*A*norm(vfx)**2/(d/20)

