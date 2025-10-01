import matplotlib.pyplot as plt
import numpy as np

years = [2005 + x for x in range(1,20,2)]
moneys = [500,700,1200,2350,1000,730,900,2000,1500,1800]
print(years,moneys)

# plt.plot(years,moneys,c='y',lw= 4,linestyle = '--')
# c = color, lw = linewidth, linestyle = dashed, normal,etc.
plt.plot(years,moneys,'r--',lw = 2)
#^ another method to plot
plt.show()