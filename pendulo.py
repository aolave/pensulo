# -*- coding: utf-8 -*-
"""
Created on Sat May 22 23:01:21 2020
@author: Cesar adrian robledo olave
"""
#Librerias
import math
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import os
st = 0    # Hora de inicio
et = 30.4 # Tiempo de finalización
ts = 0.1  # Paso del tiempo
g = 10.91 # Aceleración debido a la gravedad (m / s ^ 2)
L = 1     # Longitud del péndulo (m)
b = 0.5   # Factor de amortiguación (kg / s)
m = 1     # Masa de bob (kg)
"""
  # Ecuaciones de primer orden en una función
  teta1 es desplazamiento angular en el instante de tiempo actual
  teta2 es la velocidad angular en el instante de tiempo actual
  dheta2_dt es la aceleración angular en el instante de tiempo actual
  dteta1_dt es la tasa de cambio de desplazamiento angular en el instante de tiempo actual, es decir, igual que theta2
"""
def sim_pen_eq(t,teta):
		dteta2_dt = (-b/m)*teta[1] + (-g/L)*np.sin(teta[0])
		dteta1_dt = teta[1]
		return [dteta1_dt, dteta2_dt]
# main
teta1_ini = 0     # Desplazamiento angular inicial (rad)
teta2_ini = 4     # Velocidad angular inicial (rad / s)
teta_ini = [teta1_ini, teta2_ini]
t_span = [st,et+ts]
t = np.arange(st,et+ts,ts)
sim_points = len(t)
l = np.arange(0,sim_points,1)
teta12 = solve_ivp(sim_pen_eq, t_span, teta_ini, t_eval = t)
teta1 = teta12.y[0,:]
teta2 = teta12.y[1,:]
plt.plot(t,teta1,label= 'Desplazamiento angular (rad)')
plt.plot(t,teta2,label= 'Velocidad angular (rad/s)')
plt.xlabel('Tiempo')
plt.ylabel('Disp. Angular (rad) y Vel angular (rad/s)')
plt.legend()
plt.show()
# Simulaicion
x = L*np.sin(teta1)
y = -L*np.cos(teta1)
for point in l:
		plt.figure()
		plt.plot(x[point],y[point],'bo',markersize=20)
		plt.plot([0,x[point]], [0,y[point]])
		plt.xlim(-L-0.5,L+0.5)
		plt.ylim(-L-0.5,L+0.5)
		plt.xlabel('Eje(X) dirección')
		plt.ylabel('Eje(Y) dirección')
		filenumber = point
		filenumber=format(filenumber,"05")
		filename="salida/image{}.png".format(filenumber)
		plt.savefig(filename)
		plt.close()	