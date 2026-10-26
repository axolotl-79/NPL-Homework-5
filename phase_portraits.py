import numpy as np
import matplotlib.pyplot as plt

a=0.5

X,Y = np.meshgrid(np.linspace(-1, 1, 101),np.linspace(-1, 1, 101))

U = (1-a)*X 
V = -(1+a)*Y

fig, ax = plt.subplots(1,1, figsize=(5,5))

ax.streamplot(X,Y, U, V, density=1, linewidth=1.5)
plt.plot(0,0, '-ok', ms=5)

plt.show()