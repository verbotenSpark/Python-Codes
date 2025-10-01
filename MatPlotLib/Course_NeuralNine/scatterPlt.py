import matplotlib.pyplot as plt
import numpy as np

x_dat = np.random.random(1000)*100
y_dat = np.random.random(1000)*100

plt.scatter(x_dat,y_dat,s=100,c="#000",marker="*",alpha=0.5)
# s = size, c= color, marker = shape of individual data points, alpha = transparency
plt.show()