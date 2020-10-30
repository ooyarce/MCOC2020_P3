# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:19:04 2020
@author: Pauli
"""

from matplotlib.pylab import *
figure()
L=1.0
n=100   
dx=L/n
dt=2.
Nt=20000
K = 79.5  #m^2/s
c = 450  #J/ kg C
p = 7800  #kg/m^3
ui = 0
ud = 0
uinicial = 20
vector_diferencias_de_tiempo_alvaro_contreras = [1,5,10,50,100]
vector_posiciones = [0.104,0.208,0.416]

for posicion in vector_posiciones:
    for delta in vector_diferencias_de_tiempo_alvaro_contreras:
        time = Nt/delta
        u_function = zeros((int(time),n+1))
        u_function[:,0] = ui
        u_function[:,-1] = ud
        u_function[0,1:n] = uinicial
        alpha = (K*delta)/(c*p*(dx**2))
        for k in range(int(time)-1):
            t_value = delta*k
            for i in range(1,n):	
                u_function[k,i]+alpha*(u_function[k,i+1]-2*u_function[k,i]+u_function[k,i-1])
        time_vector = linspace(0,Nt,int(time))
        plot(time_vector,u_function[:,2], label = f"Malla 20 $Δt$={dt} (s)")	

title(f"x = {vector_posiciones}")
plt.xticks([18000,36000,54000,72000,90000],["5","10","15","20","25"])
plt.ylabel("Temperatura [C]")
plt.xlabel("Tiempo [horas]")
plt.legend()
grid()
show()