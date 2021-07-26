# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 20:10:27 2021

@author: Gael
"""

import numpy as np
import matplotlib.pyplot as plt

#CONSTANTS

G = 6.67e-11 #gravitational constant in Nm^2/kg^2
Me = 5.97e24 #mass ofthe Earth in kg
total_time = 24 * 3600 #24h in seconds, a period for geostationary orbit

radius = (total_time**2*G*Me/4/np.pi**2)**(1/3)

speed = 2.0 * np.pi * radius / total_time #starting speed in y direction

def acceleration(spacecraft_position):
    vector_to_earth = - spacecraft_position
    distance_to_earth = np.linalg.norm(spacecraft_position)
    return G*Me*vector_to_earth/(distance_to_earth**3)

h = 0.1 #initial step size

delta = 1e-5 #target accuracy

t = 0 #initial time

time = []

x = []
y = []
vx = []
vy = []

#x_vec = np.stack((x,y),axis=1)
#v_vec = np.stack((vx,vy), axis=1)


###########initial conditions#################################################

x.append(radius)
y.append(0)
vx.append(0)
vy.append(speed)


while t<total_time:
    x_vec = np.array([[x[-1], y[-1]]])
    v_vec = np.array([[vx[-1], vy[-1]]])
    acceleration0 = acceleration(x_vec)
    
    
    
    rho = 0
    while rho<1:
        xE = x_vec + h*v_vec
        vE = v_vec * h*acceleration0
        
        xH = xE + h*0.5*(v_vec + vE)
        vH = vE + h*0.5*(acceleration0 + acceleration(xE))
        
        err_x = np.linalg.norm(xE-xH)
        err_v = np.linalg.norm(vE-vH)
        
        err_total = err_x + total_time*err_v
        if(err_total==0):
            err_total = 1e-8
        rho = h * delta/ err_total
        
        h = min(h*rho**0.5, h*2)
        
    x.append(x_vec[-1,0])
    y.append(x_vec[-1,1])
    vx.append(v_vec[-1,0])
    vy.append(v_vec[-1,1])
    
    t += h
    time.append(t)
    
print(t)
    