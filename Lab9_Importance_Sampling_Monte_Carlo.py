#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"]})

N=10000
z=np.random.random(N)  # uniform random numbers
x=z**2  # non-uniform random numbers obtained from the transformation p(x)dx=q(z)dz on the [0,1] interval, when p(x)=1/(2*np.sqrt(x))
x_axis_points=np.linspace(start=0.01,stop=1, num=100)

def g(t):
    return 1*2/(np.exp(t)+1) # where 2=integral of weight over the integral (you can find g(x)=f(x)/w(x) and normalize by weight, or g(x)=f(x)/p(x) where p(x) is probability and it is normalized to 1)

def p(t):
    return 1/(2*np.sqrt(t))

integral=(1/N)*np.sum(g(x))
probability=p(x_axis_points)

f, [ax1,ax2,ax3]=plt.subplots(1, 3, figsize=(15,5))

print('The value of the integral is:', integral)
# print('z is', z)
# print('x is',x)
# print('g(x) is', g(x))

ax1.hist(z, density=True)
ax1.set_title('The normalized histogram of the uniform \n random points in the [0,1) interval')
# plt.show()
ax2.hist(x, density=True)
ax2.set_title('The normalized histogram of the transformed \n random points in the [0,1) interval')

# plt.show()
ax3.plot(probability,x_axis_points)
ax3.set_title('The probability distribution function, \n' + r' $p(x)=\frac{1}{\sqrt{2}}$ from which sample points are drawn')
plt.show()


# In[ ]:




