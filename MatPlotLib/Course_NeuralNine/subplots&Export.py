import matplotlib.pyplot as plt
import numpy as np


fig,axs = plt.subplots(2,2)

x1 = np.arange(100)
x2 = np.arange(10)
axs[0,0].plot(x2,np.cos(x2))
axs[0,0].set_title("Cos Wave")

axs[0,1].scatter(np.random.random(50),np.random.random(50))
axs[0,1].set_title("Scatter")

axs[1,0].plot(np.random.normal(50,10,10))
axs[1,0].set_title("normal")

axs[1,1].plot(x1,np.log(x1))
axs[1,1].set_title("log")

fig.suptitle("Four Plots")


plt.tight_layout() #removes overlapping of subplots
plt.savefig("Four_Plots.png",dpi = 300,transparent=False)
plt.show()