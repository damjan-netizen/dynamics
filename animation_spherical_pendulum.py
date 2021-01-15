# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 15:06:45 2021

@author: Network Damjan
"""

import pygame 
from pygame.locals import *
import sys
from math import sin,cos,pi
import numpy as np
from numpy.linalg import inv
from math import sin,cos,tan,pi

#integrator
def G(y,t):
    theta_d, phi_d = y[0], y[1]
    theta, phi = y[2],y[3]
    
    theta_dd = phi_d**2*cos(theta)*sin(theta)-g/l*sin(theta)
    phi_dd = -2.0*theta_d*phi_d/tan(theta) 
   
    return np.array([theta_dd, phi_dd, theta_d,phi_d])
    
def RK4_step(y, t, dt):
    k1 = G(y,t)
    k2 = G(y+0.5*k1*dt, t+0.5*dt)
    k3 = G(y+0.5*k2*dt, t+0.5*dt)
    k4 = G(y+k3*dt, t+dt)

    return dt * (k1 + 2*k2 + 2*k3 + k4) /6

def update(theta, phi):
    
    x = scale*l*sin(theta)*cos(phi) + offset[0]
    y = scale*l*cos(theta) + offset[1]#change of the sign was necessary because y-coodrinate is positive downwards
    z = scale*l*sin(theta)*sin(phi)
    
    
    
    return (int(x),int(y),int(z))
    
    
def render(point):
    
    x, y, z = point[0], point[1], point[2]
    z_scale =( 2 - z/(scale*l))*10.0
    
    
    
    if prev_point:
        pygame.draw.line(trace,LT_BLUE,prev_point,(x,y),int(z_scale*0.2))
    
    screen.fill(WHITE)
    if is_tracing==True:
        
        screen.blit(trace, (0,0))
    
    #draw the lines first, for layering purposes
    pygame.draw.line(screen, BLACK,offset,(x,y),int(z_scale*0.3))
    #draw the circles next, including a black circle to locate the offset
    pygame.draw.circle(screen, BLACK, offset,8)
    pygame.draw.circle(screen, BLUE, (x,y),int(m*z_scale))
    
    return (x,y)
    
    


w, h = 1024, 768

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)

LT_BLUE = (230,230,255)

offset = (w//2, h//4)  #need offset to put the pendulum at the center of the screen
scale = 100
screen = pygame.display.set_mode((w,h)) #setting the display
screen.fill(WHITE) #painting the screen white
trace = screen.copy() #making a new screen for drawing the trace

is_tracing = True #flag  for turning on/off the tracing

pygame.display.update()
clock = pygame.time.Clock() #for framerate locking


#parameters
m = 3.0
l = 4.5
g = 9.81
prev_point = None


#initial state
t = 0.0
delta_t=0.02
y = np.array([0.0,0.0,1.5,0.0])

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 38)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == KEYDOWN:
            if event.key==K_t:
                is_tracing = not(is_tracing)
            if event.key==K_c:
                trace.fill(WHITE)
                
                
    
    #update step
    point = update(y[2],y[3])
    #render step
    prev_point = render(point)

    
    
    
    text_string = f'Time: {round(t,1)} seconds'
    text = myfont.render(text_string, False, (0,0,0))
    screen.blit(text,(10,10))
    t += delta_t
    y = y + RK4_step(y, t, delta_t)
    
    
    
    clock.tick(60)
    pygame.display.update()