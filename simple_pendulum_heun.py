# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 21:06:55 2021

@author: Gael
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint



#define initial conditions
initial_angle = np.radians(45.0)
initial_velocity = 0.0
y0 = np.array([initial_angle, initial_velocity])


#parameters
g = 9.81
l = 1.0
m = 1.0

h = 0.01
time = np.arange(0, 10.0, h)

num_steps = np.size(time)

#equations
y = np.zeros([num_steps+1,2])  #state vector <theta, theta_dot>

y[0] = y0 #initial conditions

def F(y):
    theta, theta_dot = y
    F = np.array([theta_dot, -g/l * np.sin(theta)])
    return F





#integrator

def heun_integrator(y, step_size, num_steps):
    
    yE = np.zeros([num_steps+1,2])
    yE[0] = y[0]
    for i in range(num_steps):
        yE[i+1] = yE[i] + h*F(yE[i])
        y[i+1] = y[i] + h*0.5*(F(y[i])+F(yE[i]))
        
    return y

def symplectic_euler(y, step_size, num_steps):
    for i in range(num_steps):
        y[i+1,0] = y[i,0] + h*F(y[i])[0]
        y[i+1,1] = y[i,1] + h*F(y[i+1])[1]
    return y

def total_energy(y):
    num_points = np.size(y,0)
    E = np.zeros([num_points])
    for i in range(num_points):
        E[i] = 0.5*m*l**2*y[i,1]**2 + m*g*l*(1-np.cos(y[i,0]))
    return E
        
yH = heun_integrator(y, h, num_steps)
y = np.zeros([num_steps+1,2])  #state vector <theta, theta_dot>
energy_H = total_energy(yH)

y[0] = y0 #initial conditions
yS = symplectic_euler(y, h, num_steps)
energy_S = total_energy(yS)


    


#plot the results

axes = plt.gca()
axes.set_xlabel('Time in s')
axes.set_ylabel('Angle of declination $\theta$')
plt.plot(yH[:,0])
plt.plot(yS[:,0])
plt.legend(['Heun''s integrator solution', 'Symplectic Euler solution'],\
           loc='lower right')