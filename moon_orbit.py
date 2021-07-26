# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 18:32:29 2021

@author: Gael
"""

# PROBLEM 1
#
# Modify the orbit function below to model
# one revolution of the moon around the earth,
# assuming that the orbit is circular.
#
# Use the math.cos(angle) and math.sin(angle) 
# functions in order to accomplish this.

import math
import numpy as np
import matplotlib.pyplot as plt

moon_distance = 384e6 # in m

def orbit():
    num_steps = 200;
    x = np.zeros([num_steps+1,2])
    
    for n in range(num_steps+1):
        x[n,0] = moon_distance * math.cos(2*math.pi*n/num_steps)
        x[n,1] = moon_distance * math.sin(2*math.pi*n/num_steps)
        
    return x
    
x = orbit()

def plot_orbit():
    plt.axis('equal')
    plt.plot(x[:,0],x[:,1])
    axes = plt.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral postion in m')
    
    
plot_orbit()