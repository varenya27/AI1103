import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(0, 10)

plt.grid(color='grey')

plt.plot(x,3*np.exp(-3*x), color='cyan', label = '$X_{(1)}$')
plt.plot(x,6*np.exp(-2*x)*(1-np.exp(-x)), color='green', label = '$X_{(2)}$')
plt.plot(x,3*np.exp(-x)*(1-np.exp(-x))**2, color='orange', label = '$X_{(3)}$')

plt.legend()
plt.show() 
