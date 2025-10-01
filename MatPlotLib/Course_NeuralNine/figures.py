import matplotlib.pyplot as plt
import numpy as np

x1 = np.random.random(100)
y1 = np.random.random(100)

x2 = np.arange(100)
y2 = np.random.random(100)

plt.figure(1)
plt.scatter(x1,y1)

plt.figure(2)
plt.plot(x2,y2)

plt.show()