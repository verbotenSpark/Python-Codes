import matplotlib.pyplot as plt
import numpy as np
import random

headTail = [0,0]

for _ in range(10000):
    headTail[random.randint(0,1)] += 1
    plt.bar(["Heads","Tails"],headTail,color=["red","green"])
    plt.pause(0.01)
plt.show()