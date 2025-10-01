import matplotlib.pyplot as plt
import numpy as np

heights = np.random.normal(160,30,300)

plt.boxplot(heights)
plt.show()