import numpy as np 
import matplotlib.pyplot as plt

#initializing variables
theta = 20
n=1

#generating arrays:
x = np.linspace(0, 100)
y= np.linspace(-100, theta)


plt.grid(color='grey', ls=':')
plt.xlim(-10,150)
plt.ylim(-3*(theta*n/2),theta*n + 20)

#graph for Z_n:
plt.plot(x, n*((n*(np.exp((theta-x)*n)))-theta), color='cyan') 
plt.plot(y, 0*y, color='cyan')

#graph for Y_1:
plt.plot(x, n*(np.exp(n*theta-n*x)), color='orange')
plt.plot(y, 0*y, color='orange')

#some points and reference lines:
plt.plot(theta,0, 'go')
plt.plot(theta,n,'go')
plt.vlines(x=theta, ymin=-n//2, ymax=n, ls='--')

#labels:
plt.xlabel('$x$')
# plt.ylabel('$P_{Y_1}$')
plt.ylabel('$Z_{100}$')

plt.show() 
