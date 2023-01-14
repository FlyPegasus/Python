import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([1,2,3,4,5])
factpoints=np.array([1,2,6,24,120])
powerof2=np.array([2,4,8,16,32])
const=np.array([1,1,1,1,1])
square=np.array([1,4,9,16,25])
plt.plot(xpoints,factpoints)#the plot function draws a line from point to point
plt.plot(xpoints,powerof2)
plt.plot(xpoints,const)
plt.plot(xpoints,square)
plt.show()
