# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 23:22:33 2021

@author: Gael
"""

import numpy as np
import matplotlib.pyplot as plt

#initializing constants

h = 5.0 # s
mE = 5.97e24 # kg
mS = 30000. # kg
G = 6.67e-11 # N m2 / kg2
period = 24*3600 #one day in s
num_steps = 20000

x = np.zeros([num_steps+1, 2])
v = np.zeros([num_steps+1, 2])
energy = np.zeros(num_steps+1)

#initial conditions

x[0, 0] = 15e6
x[0, 1] = 1e6
v[0, 0] = 2e3
v[0, 1] = 4e3

def acceleration(spaceship_position):
    vector_to_earth = - spaceship_position # earth located at origin
    return G * mE / \
        np.linalg.norm(vector_to_earth)**3 * vector_to_earth
        

def forward_euler(x, y, step_size, num_steps):
    for i in range(num_steps):
        x[i+1] = x[i] + step_size*y[i]
        y[i+1] = y[i] + step_size*acceleration(x[i])
        
    return x, y
    

def total_energy(x, v, step_size, num_steps):
    E = np.zeros(num_steps+1)
    for i in range(num_steps+1):
        E[i] = 0.5*mS*np.linalg.norm(v[i])**2\
            -G*mE*mS/np.linalg.norm(x[i])
        
    return E

x, v = forward_euler(x,v,h, num_steps)
energy = total_energy(x,v,h,num_steps)

axes1 = plt.subplot(211)
plt.plot(x[:,0],x[:,1])
axes1.set_xlabel('Longitudinal distance in m')
axes1.set_ylabel('Lateral distance in m')
plt.axis('equal')
axes2 = plt.subplot(212)
plt.plot(energy)
axes2.set_xlabel('Step number')
axes2.set_ylabel('Total energy in J')
