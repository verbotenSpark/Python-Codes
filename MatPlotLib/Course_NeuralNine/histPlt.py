import matplotlib.pyplot as plt
import numpy as np

ages = np.random.normal(25,3,900)

# plt.hist(ages,bins=20) #specify that store all ages in 20 bins only
# plt.hist(ages,bins=[ages.min(),18,21,24,27,30,ages.max()]) # specify ranges of each bin
plt.hist(ages,bins= 10,cumulative=True) 
# cumulative gives higher numbers more data, cumulative = no of ages <= current bin
plt.show()