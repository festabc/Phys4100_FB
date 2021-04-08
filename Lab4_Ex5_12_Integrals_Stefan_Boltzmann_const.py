import numpy as np
import astropy.constants as c
import astropy.units as u
import time
import cProfile
pr = cProfile.Profile()
pr.enable()

start=time.time()

# the integrand
def f(x):
    return x**3/(np.exp(x) - 1)

# integration using Simpson's rule
def I_simpson(a,b,N):
    
    h=(b-a)/N   # N is number of slices
    
    sum_1=(f(a)+f(b))
    sum_even=0
    sum_odd=0
    
    for k in range(1,N,2):
        
        sum_odd +=f(a + k*h)
        
    for k in range(2,N,2):
        
        sum_even +=f(a + k*h)
        
    integral=(sum_1 + 4*sum_odd + 2*sum_even)*h*(1/3)
    
    return integral

# constanst in the Stefan-Boltzmann equation

    
const=(c.k_B**4)/(4*(np.pi**2)*(c.c**2)*(c.hbar**3))
#const_W=const.to_value(u.W/((u.m**2)*(u.K**4)))
    
    

# Stefan-Boltzmann constant

def SB(a,b,N):
    
    SB=const*I_simpson(a,b,N)
    error=(np.abs(c.sigma_sb-SB)/c.sigma_sb)*100
    print('The value of the integral alone is:',I_simpson(a,b,N))
    print('The value of the constants is:', const)
    print('Calculated Stefan-Boltzmann constant is:',SB)
    print ('Theoretical Stefan-Botlzmann constant is:', c.sigma_sb)
    print ('The error is: Theoretical_SB - Calculated_SB ={}  %'.format (error))
    return SB

print ('Calculated Stefan-Boltzmann constant when a=1e-10, b=100 and N=50,000 is {}'.format(SB(1e-10,100,50000)))
end=time.time()
print(f"Program took :{end-start} seconds to run")
pr.disable()
pr.print_stats(sort='time')