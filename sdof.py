import numpy as np
from numpy.linalg import inv
from matplotlib import pyplot as plt

#variables
m = 2.0
k = 2.0
c = 1.0  #critical damping = 2*sqrt(m*k) = 4.0 in this case

F0 = 1.0 #Forcing function
delta_t = 0.001
omega = 1.0
time = np.arange(0.0, 40.0,delta_t)


Y = []  #store the values of y at each time-step
force = [] #store the values of F at each time-step
#initial state
y = np.array([0,0])  #[velocity,displacement]

A = np.array([[m,0],[0,1]])
B = np.array([[c,k],[-1,0]])
F = np.array([0.0,0.0])
#time-stepping solution
for t in time:
    if t<=14:
        F[0] = F0 * np.cos(omega*t)
    else:
       F[0] = 0.0
    y = y + delta_t * inv(A).dot(F-B.dot(y))
    Y.append(y[1]) #stores displacement
    force.append(F[0]) #stores foring function
    #calculate kinetic and potential energy
    T = 0.5*m*y[0]**2
    U = 0.5*k*y[1]**2

    if t%1 <=0.01:
        print 'Total Energy:', T+U
    
    


#plot the result
t = [i for i in time]

plt.plot(t,Y)
plt.plot(t, force)
plt.grid(True)
plt.legend(['Displacement','Force'], loc='lower right')

plt.show()

print 'Critical Damping:', np.sqrt((-c**2+4*m*k)/(2.0 *m))
print 'Natural Frequency: ', np.sqrt(k/m)




