#!/usr/bin/env python
# coding: utf-8

# ## Linear and Nonlinear Equations
# Exercise 6.14:
# 
# Consider a square potential well of width w with walls of height V:
# 
# 
# Using Schroödinger’s equation, it can be shown that the allowed energies E of a single quantum particle of mass m trapped in the well are solutions of
# 
# \tan{\sqrt{w^2 m E / 2 \hbar^2}} = \sqrt{(V-E)/E}    for even numbered states
# \tan{\sqrt{w^2 m E / 2 \hbar^2}} = \sqrt{E/(V-E)}    for odd numbered states
# 
# where the states are numbered starting from 0, with the ground state being state 0, the first
# excited state being state 1, and so forth.
# 
# For an electron (mass 9.1094×10−31 kg) in a well with V = 20eV and w = 1nm, write a Python program to plot the three quantities
# y_1 = \tan{\sqrt{w^2 m E / 2 \hbar^2}}, \,\,\,\, y_2 = \sqrt{V-E\over{E}}, \,\,\,\, y_3 = -\sqrt{E\over{V-E}}
# 
# on the same graph, as a function of E from E = 0 to E = 20eV. From your plot make approximate estimates of the energies of the first six energy levels of the particle.
# 
# Write a second program to calculate the values of the first six energy levels in electron volts to an accuracy of 0.001 eV using binary search.

# In[15]:


import numpy as np
import scipy.constants as cons 
import astropy.units as u
import matplotlib.pyplot as plt
import time
import timeit
import cProfile

def main():

    # For timing purposes
    start = time.time()
    pr = cProfile.Profile()
    pr.enable()

    m=cons.m_e # mass of the electron 

    V_eV=20 # potential in eV
    V_J=20*cons.elementary_charge # potential in J

    # w=1e-9  well depth in m

    eV=cons.elementary_charge # 1eV=(1.602 * 1e-19J), conversion factor from eV to J
    hbar=cons.hbar
    h=cons.physical_constants['Planck constant in eV/Hz']
    hbar_eV=h[0]*(1/(2*np.pi))

    E_eV=np.linspace(0, 20,1000) # energy levels in eV
    E_J=E_eV*cons.elementary_charge # energy levels in J

    # The functions
    def y_tan(E, w=1e-9):
        return np.tan(np.sqrt(w**2 * m*E*(1/cons.elementary_charge)/(2*hbar_eV**2)))

    def y_even(E, V=20):
        return np.sqrt((V-E)/E)

    def y_odd(E, V=20):
        return -np.sqrt(E/(V-E))

    y1=y_tan(E_eV)
    y2=y_even(E_eV, V_eV)
    y3=y_odd(E_eV, V_eV)
    
    # The plot
    plt.plot(E_eV, y1, 'r-', label='tangent function')
    plt.plot(E_eV, y2, 'g-', label= 'even values')
    plt.plot(E_eV, y3, 'b-', label='odd values')
    plt.ylim([-20,20])
    plt.xlabel('Energy in eV')
    plt.legend(loc='upper right')
    plt.show()

    # Bisection method to find the roots
    def f_even(E):
        return y_tan(E, w=1e-9)-y_even(E, V=20)   #tangent function - even values function 

    def f_odd(E):
        return y_tan(E, w=1e-9)-y_odd(E, V=20)   #tangent function - odd values function
    
    def bisection(a,b, func, accuracy=1e-5):
    
        if (func(a)*func(b)>=0):
            print('You have not chosen the right a and b values')
            return
        
        c=a
        while ((b-a)>=accuracy):
        
            c=(a+b)/2    # find the middle point
        
            if (func(c)==0.0):   # check if the middle point is root
                break
            
            if (func(c)*func(a) < 0):  # decide which side to repeat the steps
                b=c
            
            else:
                a=c
            
        return c
    
    # The even roots
    root_even_1=bisection(2.5, 3.0, f_even)
    print ('The first root of the even numbered states is:', "%.4f"%root_even_1)
    root_even_2=bisection(7.5, 8.0, f_even)
    print ('The second root of the even numbered states is:', "%.4f"%root_even_2)
    root_even_3=bisection(14.0, 15.5, f_even)
    print ('The third root of the even numbered states is:', "%.4f"%root_even_3)
    
    # The odd roots
    root_odd_1=bisection(1.0, 1.5, f_odd)
    print ('The first root of the odd numbered states is:', "%.4f"%root_odd_1)
    root_odd_2=bisection(4.7, 5.4, f_odd)
    print ('The second root of the odd numbered states is:', "%.4f"%root_odd_2)
    root_odd_3=bisection(10.0, 12.5, f_odd)
    print ('The third root of the odd numbered states is:', "%.4f"%root_odd_3)


    pr.disable()
    # pr.print_stats(sort='time')
    end = time.time()
    print(f"Program took {end - start} seconds to run")


if __name__ == '__main__':
    main()

