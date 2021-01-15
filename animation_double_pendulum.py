import pygame 
from pygame.locals import *
import sys
from math import sin,cos,pi
import numpy as np
from numpy.linalg import inv

#integrator
def G(y,t):
    a1d, a2d = y[0], y[1]   #angular velocity definition
    a1, a2 = y[2], y[3]     #angular position
    
    #definition of the mass matrix
    m11, m12 = (m1+m2)*l1, m2*l2*np.cos(a1-a2)
    m21, m22 = l1*np.cos(a1-a2), l2
    M = np.array([[m11,m12],[m21,m22]])
    
    #definiton of the force matrix
    f1 = -m2*l2*a2d*a2d*np.sin(a1-a2)-(m1+m2)*g*np.sin(a1)
    f2 = l1*a1d*a1d*np.sin(a1-a2)-g*np.sin(a2)
    F = np.array([f1,f2])
    
    accel = inv(M).dot(F)
    return np.array([accel[0], accel[1], a1d, a2d])
    
def RK4_step(y, t, dt):
    k1 = G(y,t)
    k2 = G(y+0.5*k1*dt, t+0.5*dt)
    k3 = G(y+0.5*k2*dt, t+0.5*dt)
    k4 = G(y+k3*dt, t+dt)

    return dt * (k1 + 2*k2 + 2*k3 + k4) /6

def update(a1, a2):
    scale = 100     #we need this to convert from meters to pixels
    
    x1 = l1*scale*sin(a1) + offset[0]
    y1 = l1*scale*cos(a1) + offset[1]
    
    x2 = x1 + l2*scale*sin(a2)
    y2 = y1 + l2*scale*cos(a2)
    
    return (x1,y1), (x2,y2)
    
    
def render(point1, point2):
    
    x1,y1 = int(point1[0]), int(point1[1])
    x2,y2 = int(point2[0]),int( point2[1])
    
    if prev_point:
        xp, yp = prev_point[0], prev_point[1]
        pygame.draw.line(trace,LT_BLUE,(xp,yp),(x2,y2),3)
    
    screen.fill(WHITE)
    screen.blit(trace, (0,0))
    scale = 10
    #draw the lines first, for layering purposes
    pygame.draw.line(screen, BLACK,offset,(x1,y1),5)
    pygame.draw.line(screen, BLACK,(x1,y1),(x2,y2),5)
    #draw the circles next, including a black circle to locate the offset
    pygame.draw.circle(screen, RED, (x1,y1), int(m1*scale))
    pygame.draw.circle(screen, BLACK, offset,8)
    pygame.draw.circle(screen, BLUE, (x2,y2), int(m2*scale))
    
    return (x2,y2)
    
    


w, h = 800, 600

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)

LT_BLUE = (230,230,255)

offset = (400, 50)  #need offset to put the pendulum at the center of the screen

screen = pygame.display.set_mode((w,h)) #setting the display
screen.fill(WHITE) #painting the screen white
trace = screen.copy() #making a new screen for drawing the trace

pygame.display.update()
clock = pygame.time.Clock() #for framerate locking


#parameters

m1, m2 = 3.0, 2.0
l1, l2 = 1.5, 2.0
g = 9.81
prev_point = None


#initial state
t = 0.0
delta_t=0.02
y = np.array([0.0,0.0,2.0,1.0])

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 38)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
                
    
    #update step
    point1, point2 = update(y[2],y[3])
    
    prev_point = render(point1, point2)

    #render step
    render(point1, point2)
    
    text_string = f'Time: {round(t,1)} seconds'
    text = myfont.render(text_string, False, (0,0,0))
    screen.blit(text,(10,10))
    t += delta_t
    y = y + RK4_step(y, t, delta_t)
    
    
    
    clock.tick(60)
    pygame.display.update()