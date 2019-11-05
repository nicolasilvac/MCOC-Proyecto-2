from matplotlib.pylab import * 

#
from Parametros import *
from Funciones import *

import time
import random

reuse_initial_condition=True
#reuse_initial_condition=False
doit=True
#doit=False
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

import h5py

fout = h5py.File("Resultados.hdf5", "w")

fout_parametros = fout.create_group("parametros")

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
#print Nt
#exit(0)
done=zeros(Nparticulas,dtype=int32)
impacting_set = zeros(Nparticulas,dtype=int32)

print "Integrating"
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
		#zk=z[k,:]
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
fout.close()

Final = time.time()

print tiempo_bloque_1
print tiempo_bloque_2
print 'Tiempo Total:', Final - Inicio

