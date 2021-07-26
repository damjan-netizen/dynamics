# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 21:22:11 2021

@author: Gael
"""

import numpy as np
import matplotlib.pyplot as plt
import math

h_array = []
err_array_euler = []
err_array_heun = []

#CONSTANTS

G = 6.67e-11 #gravitational constant in Nm^2/kg^2
Me = 5.97e24 #mass ofthe Earth in kg
total_time = 24 * 3600 #24h in seconds, a period for geostationary orbit

radius = (total_time**2*G*Me/4/math.pi**2)**(1/3)

speed = 2.0 * math.pi * radius / total_time #starting speed in y direction

def acceleration(spacecraft_position):
    vector_to_earth = - spacecraft_position
    distance_to_earth = np.linalg.norm(spacecraft_position)
    return G*Me*vector_to_earth/(distance_to_earth**3)

def calculate_error(num_steps):
    h = total_time/num_steps
    
    x = np.zeros([num_steps+1, 2])
    v = np.zeros([num_steps+1, 2])
    
    x[0,0] = radius #initialize the position along the orbit
    v[0,1] = speed #initialize the y velocity component
    #Begin Euler's method
    for i in range(num_steps):
        x[i+1] = x[i] + h*v[i]
        v[i+1] = v[i] + h*acceleration(x[i])
        
    err_euler = np.linalg.norm(x[-1]-x[0])
    err_array_euler.append(err_euler)
    h_array.append(h)
    
    #Euler's Method end
    
    #Heun's Method begin
    
    for i in range(num_steps):
        xE = x[i] + h*v[i]
        vE = v[i] + h*acceleration(x[i])
        
        x[i+1] = x[i] + h*(v[i]+vE)/2
        v[i+1] = v[i] + h*(acceleration(x[i])+acceleration(xE))/2
        
    err_heun = np.linalg.norm(x[-1]-x[0])
    err_array_heun.append(err_heun)
    
    return x, v, err_euler, err_heun

for num_steps in [200, 500, 1000, 2000, 5000, 10000]:
    x, v, err_euler, err_heun = calculate_error(num_steps)

def plot_me():
    plt.figure(1)
    axes = plt.gca()
    axes.set_xlabel('Step size in s')
    axes.set_ylabel('Error in m')
    plt.scatter(h_array,err_array_euler)
    plt.scatter(h_array, err_array_heun,color='r')
    plt.xlim(xmin=0.)
    plt.ylim(ymin=0.)
    
    
    
    
    
    
print(x)
plot_me()