import numpy as np
from matplotlib import pyplot as plt
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

   


#variables
m1, m2 = 2.0, 1.0
l1, l2 = 1.0, 2.0
g = 9.81

delta_t = 0.01
time = np.arange(0.0, 10.0, delta_t)

Y1 = [] #storage for theta1
Y2 = [] #storage for theta2


#initial state

y = np.array([0,0,0,1.0])




#time_stepping
for t in time:
    y = y + RK4_step(y, t, delta_t)
    
    Y1.append(y[2])
    Y2.append(y[3])
    


#plotting

plt.plot(time,Y1)
plt.plot(time,Y2)
plt.grid(True)
plt.legend([r'$\theta_1$', r'$\theta_2$'], loc = 'lower right')
plt.show()
