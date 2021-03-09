#!/usr/bin/env python
# coding: utf-8

# ## Exercise 3.2: Curve plotting
# 
# Although the plot function is designed primarily for plotting standard xy graphs, it can be adapted for other kinds of plotting as well.
# 
# a)  Make a plot of the so-called deltoid curve, which is defined parametrically by the equations, x = 2 cos θ + cos 2θ, y = 2 sin θ − sin 2θ, where 0 ≤ θ < 2π. Take a set of values of θ between zero and 2π and calculate x and y for each from the equations above, then plot y as a function of x.
# 
# b)  Taking this approach a step further, one can make a polar plot r = f(θ) for some function f by calculating r for a range of values of θ and then converting r and θ to Cartesian coordinates using the standard equations x = r cos θ, y = r sin θ. Use this method to make a plot of the Galilean spiral, r=θ2 for 0 ≤ θ ≤ 10π.
# 
# c)  Using the same method, make a polar plot of “Fey’s function”
# r = e^{\cos{\theta}} - 2 \cos{4 \theta} + \sin^5{\frac{\theta}{12}} 
# 
# 
# 

# In[28]:


import numpy as np
import matplotlib.pyplot as plt
import sys

def figures():
  
    # Deltoid
    
    theta=np.linspace(0, 2*np.pi, 500)
    x = 2*np.cos(theta) + np.cos(2*theta)
    y = 2*np.sin(theta) - np.sin(2*theta)
    
    fig1=plt.figure()
    fig1=plt.plot(x,y,linestyle='-',color='b')
    #plt.show()

    # Galilean spiral
    
    theta=np.linspace(0, 10*np.pi, 500)
    r=theta**2
    x=r*np.cos(theta)
    y=r*np.sin(theta)
    
    fig2=plt.figure()
    fig2=plt.plot(x,y,linestyle='-',color='r')
    #plt.show()
    
    # Fey's func
    
    theta=np.linspace(0, 50*np.pi, 5000)
    alfa=4*theta
    beta=theta/12
    r=np.exp(np.cos(theta))-2*np.cos(alfa)+(np.sin(beta))**5
    x=r*np.cos(theta)
    y=r*np.sin(theta)
    
   # print('x:', x)
   # print ('y:',y)
    fig3=plt.figure()
    fig3=plt.plot(x,y,linestyle='-',color='g')
    #plt.show()
    
    # Show the three figures
    
    fig, (fig1, fig2, fig3) = plt.subplot(1, 2, 3)
    
    fig.suptitle('Deltoid, Galilean spiral, Fey function')
    #plt.show()
    
if __name__=="__main__":
    figures()


# In[29]:


#figures()


# In[ ]:




