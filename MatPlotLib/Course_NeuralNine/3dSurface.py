import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes(projection="3d")
x = np.arange(-5,5,0.1)
y = np.arange(-8,2,0.2)

X,Y = np.meshgrid(x,y)
Z = np.sin(X) * np.cos(Y)

ax.plot_surface(X,Y,Z,cmap="Spectral")
ax.set_title("SinCos Spectral")
ax.view_init(azim=45,elev= 45,roll=0)
plt.show()