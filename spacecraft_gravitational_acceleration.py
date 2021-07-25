# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 18:17:49 2021

@author: Gael
"""

import numpy as np
import matplotlib.pyplot as plt

earth_mass = 5.97e24 # kg
moon_mass = 7.35e22 # kg
gravitational_constant = 6.67e-11 # N m2 / kg2

# The origin, or (0,0), is at the center of the earth 
# in this example, so it doesn't make any sense to 
# set either the moon_position or spaceship_position
# equal to (0,0). Depending on your solution, doing this
# may throw an error!  Please note that moon_position and 
# spaceship_position are both numpy arrays, and the 
# returned value should also be a numpy array.

def acceleration(moon_position, spaceship_position):
    
    earth_distance = np.linalg.norm(spaceship_position)
    moon_distance = np.linalg.norm(moon_position-spaceship_position)
    
    e_E = (-1)*spaceship_position / earth_distance  #unit vector towards Earth
    e_M = (moon_position - spaceship_position)/moon_distance #unit vecor towards the Moon
    
    
    return gravitational_constant * ((earth_mass * e_E)/earth_distance**2 + (moon_mass*e_M)/moon_distance**2)
    