# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:19:04 2020

@author: Pauli
"""

from matplotlib.pylab import *

L=1.0
n=100   #discretizacion de intervalos
dx=L/n

x=linspace(0,L,n+1)

# Arreglo con la solución 
dt=2.
Nt=20000
u_k = zeros((n+1))
u_km1 = zeros((n+1))


#Condicion inicial 
u_k[:]=20

K = 79.5  #m^2/s
c = 450  #J/ kg C
p = 7800  #kg/m^3
alpha = (K*dt)/(c*p*(dx**2))


for k in range(Nt-1):
    t = dt*k
    print(f"k={k} t={t}")
    
    #Condiciones de borde
    u_k[-1] = 20          #Borde der
    u_k[0] = u_k[1]- 5 * dx  #Borde izq
    
 
    for i in range(1,n):
        u_km1[i] = u_k[i] + (alpha*(u_k[i+1] - 2*u_k[i] + u_k[i-1]))
    
    Nplot=1000
    Nskip=3    
    if k % Nplot == 0:     #Graficar cada 1000 pasos
        plot(x,u_k[:])
    
    if k % (Nskip*Nplot) == 0:
        text(x[0],u_k[0],f"{t/3600:.1f}",
             fontsize=8,
             horizontalalignment="center",
             verticalalignment="center",
             ).set_bbox(dict(facecolor='white', alpha=0.4, edgecolor='black',boxstyle='round'))
    u_k = u_km1 
           
title("k={}     t= {} s". format(k, k*dt)) 
xlabel("Distancia, $x$ (m)")
ylabel("Temperature, $T$ (°C)")  
show()