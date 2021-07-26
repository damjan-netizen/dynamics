# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 17:05:00 2021

@author: Gael
"""

import numpy as np
import matplotlib.pyplot as plt
import math

def forward_euler():
    h = 0.1 #time step
    g = -9.81 #m/s^2
    
    num_steps = 50
    
    t = np.zeros(num_steps+1)
    x = np.zeros(num_steps+1)
    v = np.zeros(num_steps+1)
    
    for step in range(num_steps):
        t[step+1] = (step + 1)*h
        x[step+1] = x[step] + h*v[step]
        v[step+1] = v[step] + h*g
        
    return t, x, v

# t, x, v = forward_euler()

# print("These are the results : {}, {}, {}".format(t,x,v))

# def plot_me():
#     axes_x = plt.subplot(211)
#     plt.plot(t,x)
#     axes_vel = plt.subplot(212)
#     plt.plot(t,v)
#     axes_x.set_ylabel('Height in m')
#     axes_vel.set_ylabel('Velocity in m/s')
#     axes_vel.set_xlabel('Time in s')
    


#plot_me()

# PROBLEM 2
#
# Modify the trajectory function below to 
# plot the trajectory of several particles. 
# Each trajectory starts at the point (0,0) 
# given initial speed in the direction 
# specified by the angle. Use the Forward 
# Euler Method to accomplish this.



h = 0.3 # s
g = 9.81 # m / s2
acceleration = np.array([0., -g])
initial_speed = 20. # m / s


def trajectory():
    angles = np.linspace(20., 70., 6)

    num_steps = 30
    x = np.zeros([num_steps + 1, 2])
    v = np.zeros([num_steps + 1, 2])

    for angle in angles:
        angle_rad = math.pi/180.0 * angle
        
        x[0,0] = 0.0
        x[0,1] = 0.0
        v[0,0] = initial_speed * math.cos(angle_rad)
        v[0,1] = initial_speed * math.sin(angle_rad)
        for i in range(num_steps):
            x[i+1,0] = x[i,0] + h*v[i,0]
            x[i+1,1] = x[i,1] + h*v[i,1]
            v[i+1,0] = v[i,0] + h*acceleration[0]
            v[i+1,1] = v[i,1] + h*acceleration[1]

    plt.plot(x[:, 0], x[:, 1])
    plt.axis('equal')
    axes = plt.gca()
    axes.set_xlabel('Horizontal position in m')
    axes.set_ylabel('Vertical position in m')
    return x, v

trajectory()



    
    