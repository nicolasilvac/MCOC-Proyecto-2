from matplotlib.pylab import * 
import time
import h5py

#Numero de particulas
Nparticulas = 100	

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
dt = 0.00001*_s    	# paso de tiempo 
tmax = 0.1*_s      # tiempo maximo de simulacion

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

norm = lambda v: sqrt(dot(v,v))

def propiedades_area_volumen_masa(d):
	area= pi * (d/2) ** 2
	vol = (4./3.) * pi * (d/2) ** 3
	masa = rho_particula * vol
	return area, vol, masa

def fuerzas_hidrodinamicas(x,v,d,area,masa):

	xtop = x + (d/2)*jhat
	xbot = x - (d/2)*jhat
	vf = velocity_field(x + 0*jhat)
	vrelf_top = abs(velocity_field(xtop)[0])
	vrelf_bot = abs(velocity_field(xbot)[0])
	vrel = vf - v

	Cd = 0.47
	fD = (0.5*Cd*alpha*rho_agua*norm(vrel)*area)*vrel

	fL = (0.5*CL*alpha*rho_agua*(vrelf_top - vrelf_bot)*area)*vrel[0]*jhat
	fW = (-masa*g)*jhat

	Fh = fW + fD + fL

	return Fh

def fuerza_impacto_suelo(x,v,d):
	N = around(x[0]/d)
	r = x - (N * d) * ihat
	delta = norm(r)- d
	if delta < 0:
		n = r/ norm(r)
		Fi = -k_penal * delta * n
	else:
		Fi = 0. * r 
	return Fi

def zp_una_particula(z,t,d=d):
	zp = zeros(4)

	x = z[0:2]
	v = z[2:4]

	area, vol, masa = propiedades_area_volumen_masa(d)
	Fh = fuerzas_hidrodinamicas(x,v,d,area,masa)
	Fi = fuerza_impacto_suelo(x,v,d)

	sumaF = Fh + Fi

	zp[0:2] = v
	zp[2:4] = sumaF/masa

	return zp

def zp_todas_las_particulas(z,t):
	zp = zeros(4 * Nparticulas)

	for i in range(Nparticulas):
		di = d
		xi = z[4 * i: (4 * i + 2)]
		vi = z[4 * i + 2 : (4*i +4)]

		area,vol,masa = propiedades_area_volumen_masa(d)
		Fh = fuerzas_hidrodinamicas(x,v,d,area,masa)
		Fi = fuerza_impacto_suelo(x,v,d)

		sumaF = Fh + Fi

		zp[4*i:(4*i+2)] = vi
		zp[4*i+2:(4*i+4)] = sumaF/masa   # decia m

	zp += zp_choque_M_particula(z,t,M = Nparticulas)

	return zp


def zp_M_particulas(z,t,M):
	zp = zeros(4*M)

	for i in range(M):
		di = d
		zi = z[4*i:(4*i+4)]
		vi = z[4*i+2:(4*i+4)]

		zp[4*i:(4*i+4)] = zp_una_particula(zi,t,di)

	zp += zp_choque_M_particula(z,t,M=M)

	return z|p


def zp_choque_M_particulas(z,t,M):
	zp = zeros(4*M)
	for i in range(M):
		xi = z[4*i:(4*i+2)]
		di = d
		area_i,vol_i,masa_i = propiedades_area_vol_masa(di)
		for j in range(i+1,M):
			xj = z[4*j:(4*j+2)]
			dj = d
			rij = xj - xi
			norm_rij = norm(rij)
			if norm_rij < 0.5*(di+dj):
				area_j,vol_j,masa_j = propiedades_area_vol_masa(dj)
				delta = 0.5 * (di+dj) - norm_rij
				nij = rij / norm_rij
				Fj = k_penal * delta * nij
				Fi = -Fj
				zp[4*i+2:(4*i-4)] += Fi/masa_i
				zp[4*j+2:(4*j+4)] += Fj/masa_j
	return zp


reuse_initial_condition=False

doit=True

Inicio= time.time()
tiempo_bloque_1=0
tiempo_bloque_2=0
t=arange(0,tmax,dt)
Nt=len(t)

fout=open("resultados.txt","w")

if reuse_initial_condition:
	print "Reusing initial conditions"
	data = load("initial_conditions.npz")
	x0=data["x0"]
	y0=data["y0"]
	vx0=data["vx0"]
	vy0=data["vy0"]
	Nparticulas = data["Nparticulas"]
else:
	print "Generating new initial conditions"
	itry=1
	while True:
		dmin=infty
		x0=800*d*rand(Nparticulas)
		y0=5*d*rand(Nparticulas) + 1*d
		for i in range(Nparticulas):
			xi,yi=x0[i],y0[i]
			for j in range(i+1,Nparticulas):
				xj,yj=x0[j],y0[j]
				dij=sqrt((xi-xj)**2+(yi-yj)**2)
				dmin=min(dmin,dij)
		print "Try # ", itry, "dmin/d = ", dmin/d
		if dmin >0.9*d:
			break
		itry +=1
	vx0 = ustar*rand(Nparticulas)
	vy0 = 0
	savez("Initial_condition.npz",x0=x0,y0=y0,vx0=vx0,vy0=vy0, Nparticulas=Nparticulas)
#0.14/0.15e-3	1.40.15e-3 = 9333.33
t=arange(0,tmax,dt)
Nt=len(t)
from scipy.integrate import odeint

#z=zeros((nt,Nparticulas))
zk = zeros((4*Nparticulas))
zkm1= zeros((4*Nparticulas))

zk[0::4]=x0
zk[1::4]=y0
zk[2::4]=vx0
zk[3::4]=vy0


#pasar los datos a binario con hdf5 para optimizacion de memoria
fout = h5py.File("binario_hdf5", "w")
fout_parametros = fout.create_group("Parametros")
fout_parametros["dt"] = dt
fout_parametros["g"] = g
fout_parametros["d"] = d
fout_parametros["rho_agua"] = rho_agua
fout_parametros["rho_particula"] = rho_particula
fout_parametros["tmax"] = tmax
fout_parametros["Cd"] = Cd
fout_parametros["Cm"] = Cm
fout_parametros["CL"] = CL
fout_parametros["Rp"] = Rp
fout_parametros["ustar"] = ustar
fout_parametros["tau_star"] = tau_star
fout_parametros["R"] = R
fout_parametros["alpha"] = alpha
fout_parametros["ihat"] = ihat
fout_parametros["jhat"] = jhat
fout_parametros["tau_cr"] = tau_cr
fout_parametros["A"] = A
fout_parametros["k_penal"] = k_penal
fout_z = fout.create_dataset("z",(Nt, 1+ 4*Nparticulas), dtype=double)

done=zeros(Nparticulas, dtype=int32)
impacting_set = zeros(Nparticulas, dtype=int32)

print "Integrando"
k=0

if doit:
	while dt*k<int(tmax/dt-1)*dt:

		#guarda el tiempo y los suma para el bloque de particulas que no chocan
		t_actual = time.time()
		fout_z[k,0] = dt*k
		fout_z[k,1:] = zk
		t_iteracion = time.time()
		tiempo_bloque_1 += t_iteracion - t_actual


		if k % 100==0:
			print "k={} t= {}".format(k,k*dt)
		done *= 0

		#guarda el tiempo y los suma para el bloque de particulas que chocan
		t_actual = time.time()

		for i in range(Nparticulas):
			irange = slice(4*i, 4*i+4)
			zk_i=zk[irange]
			di=d
			if done[i]==0:
				hay_impacto=False
				impacting_set *=0
				M = 1
				for j in range(i+1,Nparticulas):
					jrange = slice(4*j,4*j+4)
					zk_j=zk[jrange]
					dj=d
					rij=zk_j[0:2]-zk_i[0:2]
					if norm(rij)<0.5*(di-dj)*3:
						hay_impacto=True
						impacting_set[0]=i
						impacting_set[M]=j
						M+=1
				if hay_impacto:
					zk_all=zk_i
					for j in impacting_set[1:M]:
						jrange=slice(4*j,4*j+4)
						zk_j = zk[jrange]
						zk_all=hstack((zk_all,zk_j))
					ti=time.time()
					zkm1_all=odeint(zp_M_particulas, zk_all, [dt*k,dt*(k+1)],args=(M,))
					zkm1[irange]=zkm1_all[1,0:4]
					tf=time.time()
					tiempo_bloque_1+=tf-ti
					done[i]=pos_j=1
					for j in impacting_set[1:M]:
						jrange=slice(4*j,4*j+4)
						zkm1[jrange]=zkm1_all[1,4*pos_j:4*pos_j+4]
						done[i]=1
						pos_j+=1
				else:
					zkm1_i=odeint(zp_una_particula,zk_i,[dt*k,dt*(k+1)])
					zkm1[irange]=zkm1_i[1,0:4]
					done[i]=1
		t_iteracion = time.time()
		tiempo_bloque_2 += t_iteracion - t_actual

		zk=zkm1
		k+=1

Final = time.time()
fout.close()
print 'Tiempo bloque 1, particulas que no chocan= ',tiempo_bloque_1
print 'Tiempo bloque 2, particulas que chocan= ',tiempo_bloque_2
print 'Tiempo Total:', Final - Inicio


with h5py.File("binario_hdf5", 'r') as f:
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[1]
    data = list(f["z"])

d = 0.15e-3 

Nparticulas = (len(data[0]) -1) /4

figure()

color = "006B93"
plt = gca()
colorlist = []
xi =[]
yi =[]

#para cada particula
for i in range(Nparticulas):
	#para cada particula guarda la trayectoria
	for j in range(len(data)-1):
		xi.append(data[j][1 + 4*i] / d)
		yi.append(data[j][1 + 4*i + 1] / d)
	
	col=rand(4)
	colorlist.append(col)
	plt.plot(xi[0::100],yi[0::100],"o",color=col)
	plt.plot(xi,yi,"--",color=col,alpha=0.6)
	xi = []
	yi = []

plt.set_ylim([0,8])
plt.axhline(0.,color="k",linestyle="--")
plt.axhline(1/30.,color="gray",linestyle="--")
plt.set_xlabel("${x}/{d}$")
plt.set_ylabel("${z}/{d}$")
if Nparticulas == 1:
	titulo = 'TRAYECTORIA DE {} PARTICULA'.format(Nparticulas)
else:
	titulo = 'TRAYECTORIA DE {} PARTICULAS'.format(Nparticulas)
plt.set_title(titulo)
tight_layout()

nombre_png = 'Grafico {} particulas'.format(Nparticulas)
savefig(nombre_png)

show()