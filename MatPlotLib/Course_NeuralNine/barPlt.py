import matplotlib.pyplot as plt
import numpy as np

lang = ["java","c","Python","GO","C++","Rust"]
votes = np.random.randint(5,100,6)

plt.bar(lang,votes,width = 0.7,color='green',align="center",edgecolor = 'red', linewidth = 3)
# width = barwidth, linewidth = edgecolor width, align = start of the bar or center
plt.show()