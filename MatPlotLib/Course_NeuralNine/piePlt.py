import matplotlib.pyplot as plt
import numpy as np

category = ["veryLow","low","Healthy","High","Very High"]
peopleWeight = [20,40,90,30,10]
explodes = [0,0.1,0.2,0.1,0]

plt.pie(peopleWeight,labels=category,explode=explodes,autopct="%.2f%%",pctdistance=0.8,startangle=-90)
plt.show()