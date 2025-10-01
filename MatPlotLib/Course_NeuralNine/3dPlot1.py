import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes(projection = "3d")

x = np.random.random(100)
y = np.random.random(100)
z = np.random.random(100)

ax.scatter(x,y,z)
ax.set_title("3D Scatter Plot")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.show()