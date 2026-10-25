import numpy as np
import matplotlib.pyplot as plt

a=0.5

X,Y = np.meshgrid(np.linspace(-3, 3, 101),np.linspace(-3, 3, 101))

U = (a*np.sin(X)+np.sin(Y))*np.cos(X) 
V = (-np.sin(X)+a*np.sin(Y))*np.cos(Y) 

fig, ax = plt.subplots(1,1, figsize=(5,5))

ax.streamplot(X,Y, U, V, density=2, linewidth=1.5)

sqr = np.array([[np.pi/2, np.pi/2], [np.pi/2, -np.pi/2], [-np.pi/2, -np.pi/2], [-np.pi/2, np.pi/2], [np.pi/2, np.pi/2]])
ax.plot(sqr[:, 0], sqr[:, 1], 'g', lw=1)

plt.show()