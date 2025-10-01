import matplotlib.pyplot as plt
import numpy as np

stock1 = np.random.normal(100,3,5)
stock2 = np.random.normal(98,9,5)
stock3 = np.random.normal(101,2,5)
years = [2014 + x for x in range(5)]
plt.title("Stock Prices of 3 companies")
plt.plot(years,stock1,label="Company1",lw=4,alpha = 0.7)
plt.plot(years,stock2,label='Company2',lw=3,alpha = 0.7)
plt.plot(years,stock3,label='Company3',lw=2,alpha = 0.7)
plt.xlabel("Year")
plt.ylabel("Stock Price in USD")
plt.legend(loc="upper left")
plt.show()
