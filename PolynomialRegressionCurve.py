import numpy as np
import matplotlib.pyplot as plt

x = [0,20,40,60,80,100]
y = [0.0002,0.0012,0.006,0.03,0.09,0.27]

model = np.poly1d(np.polyfit(x,y,20))
                  
line = np.linspace(1, 100)

plt.scatter(x,y)
plt.plot(line, model(line))
plt.show()