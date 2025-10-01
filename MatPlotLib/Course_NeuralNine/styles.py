import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

style.use("dark_background")

votes = np.random.randint(5,35,6)
candidates = [chr(c) for c in range(ord("a"),ord("f"))]
plt.pie(votes,labels=None)
plt.legend(candidates,loc="upper right")
plt.show()
# print(candidates)