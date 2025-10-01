import matplotlib.pyplot as plt
import numpy as np

heights = [78,82,95,110,135,150,160,170,175,180,185]
ages = [10 + x for x in range(0,11)]
height_ticks = [x for x in range(75,190,10)]

plt.plot(ages,heights,c='g')
plt.title("Height of subject X wrt age",fontsize = 17)
plt.xlabel("Age in Years old",fontsize = 12)
plt.ylabel("Height in Cm",fontsize = 12,c="purple")
plt.yticks(height_ticks, [f"{x}cm" for x in height_ticks])
plt.show()