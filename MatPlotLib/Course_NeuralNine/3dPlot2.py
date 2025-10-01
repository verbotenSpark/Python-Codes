import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes(projection = "3d")

x = np.arange(0,100,0.1)
y = np.sin(x)
z = np.cos(x)

ax.plot(x,y,z)
ax.set_title("3D Scatter Plot")

plt.show()