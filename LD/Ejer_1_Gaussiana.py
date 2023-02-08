import matplotlib.pyplot as plt
import numpy as np
import math
def dn(x , mean, sigma):
    return np.exp(-1*((x-mean)**2)/(2*(sigma**2)))/(math.sqrt(2*np.pi) * sigma)
mean, sigma = 0,2
x = np.linspace(mean - 6*sigma, mean+6*sigma,100)
y = dn(x,mean,sigma)
plt.title("Trapecio")
plt.plot(x,y)
plt.ylabel("Eje X")
plt.xlabel("Eje Y")
plt.show()
