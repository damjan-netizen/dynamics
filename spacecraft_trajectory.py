# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 19:51:16 2021

@author: Gael
"""

# PROBLEM 3
#
# Modify the below functions acceleration and 
# ship_trajectory to plot the trajectory of a 
# spacecraft with the given initial position 
# and velocity. Use the Forward Euler Method 
# to accomplish this.

import numpy
import matplotlib.pyplot
import math

h = 0.1 # s
earth_mass = 5.97e24 # kg
gravitational_constant = 6.67e-11 # N m2 / kg2

def acceleration(spaceship_position):
    unit_vec_ss = numpy.linalg.norm(spaceship_position)
    
    return (gravitational_constant * earth_mass * (-1) * 
            spaceship_position / unit_vec_ss**3)

def ship_trajectory():
    num_steps = 130000
    x = numpy.zeros([num_steps + 1, 2]) # m
    v = numpy.zeros([num_steps + 1, 2]) # m / s

    x[0, 0] = 15e6
    x[0, 1] = 1e6
    v[0, 0] = 2e3
    v[0, 1] = 4e3
    
    for i in range(num_steps):
	    x[i+1] = x[i] + h*v[i]
	    v[i+1] = v[i] + h*acceleration(x[i])

	
	

    return x, v

x, v = ship_trajectory()


def plot_me():
    matplotlib.pyplot.plot(x[:,0],x[:,1])
    matplotlib.pyplot.scatter(0, 0)
    matplotlib.pyplot.axes('equal')
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
    
    
plot_me()
    


