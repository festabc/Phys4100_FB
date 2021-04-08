#!/usr/bin/env python
# coding: utf-8

# ## Differentiation
# 5.21: Electric field of a charge distribution:
# Suppose we have a distribution of charges and we want to calculate the resulting electric field. One way to do this is to first calculate the electric potential φ and then take its gradient. For a point charge q at the origin, the electric potential at a distance r from the origin is
# 
# \Phi = {q\over{4\pi\epsilon_0 r}} 
# 
# and the electric field is E = −∇φ.
# 
# You have two charges, of ±1 C, 10 cm apart. Calculate the resulting electric potential on a 1 m × 1 m square plane surrounding the charges and passing through them. Calculate the potential at 1 cm spaced points in a grid and make a visualization on the screen of the potential using a density plot.
# Now calculate the partial derivatives of the potential with respect to x and y and hence find the electric field in the xy plane. Make a visualization of the field also. This is a little trickier than visualizing the potential, because the electric field has both magnitude and direction. One way to do it might be to make two density plots, one for the magnitude, and one for the direction, the latter using the “hsv” color scheme in pylab, which is a rainbow scheme that passes through all the colors but starts and ends with the same shade of red, which makes it suitable for representing things like directions or angles that go around the full circle and end up where they started. A more sophisticated visualization might use the arrow object from the visual package, drawing a grid of arrows with direction and length chosen to represent the field.

# In[74]:


import numpy as np
import astropy.constants as c
import scipy.constants as cons
import matplotlib.pyplot as plt

# the charges
q1=1   #in Coulombs
q2=-1  # in Coulombs

# the potential
def V(q,distance): 
    return q/(4*np.pi*cons.epsilon_0*distance)

# the coordinate system and charge coordinates

x=np.linspace(0,100,100)
y=np.linspace(0,100,100)
x_coords, y_coords = np.meshgrid(x, y, indexing='xy')
p1_coord=[45,50]  # Point 1 coordinates, q1=1C
p2_coord=[55,50]  # Point 2 coordinates, q2=-1C


# The origin
origin=[0,0]

# Any other point
r=[x_coords,y_coords]


# r1=np.sqrt((p1_coord[1]-origin[1])**2 + (p1_coord[0]-origin[0])**2) # Distance from origin to first charge, q1=1C
# r2=np.sqrt((p2_coord[1]-origin[1])**2 + (p2_coord[0]-origin[0])**2) # Distance from origin to first charge, q2=-1C


r_1=np.sqrt((p1_coord[1]-r[1])**2 + (p1_coord[0]-r[0])**2) # Distance from first charge to any other point, q1=1C
r_2=np.sqrt((p2_coord[1]-r[1])**2 + (p2_coord[0]-r[0])**2) # Distance from second charge to any other point, q2=-1C

# The total potential of the two charges

V_tot = V(q1,r_1) + V(q2,r_2)

fig,[ax1, ax2]=plt.subplots(nrows=1,ncols=2,figsize=(15,5))

#plt.plot(phi())
#ax1.contour(V_tot)
#ax1.imshow(V_tot)
CS=ax1.contour(x_coords, y_coords, V_tot, 700)
ax1.set_title('The potential of two charges, q1=1C and q2=-1C')
ax1.set_xlabel('x-axis (cm)')
ax1.set_ylabel('y-axis (cm)')
levels = [-1.5, -1, -0.5, 0, 0.5, 1]
#CS2 = ax1.contour(CS, levels=CS.levels[::2], colors=('r', 'g', 'b'), extend='both')
ax1.clabel(CS, fmt='%2.1f', colors='k', fontsize=9)


# The electric field

h=1e-5
const=4*np.pi*cons.epsilon_0
def distance(x,y):
    
    return np.sqrt((r[0]-x)**2 + (r[1]-y)**2) # Distance 

def E_x(q,x,y):
    
    return (q/const)*(-1/distance(x,y)**2)*(1/h)*(distance(x+h/2,y)-distance(x-h/2,y))

def E_y(q,x,y):
    
    return (q/const)*(-1/distance(x,y)**2)*(1/h)*(distance(x,y + h/2)-distance(x,y - h/2))

# Electric field x and y components for first charge
E1_x=E_x(q1,p1_coord[0],p1_coord[1])   
E1_y=E_y(q1,p1_coord[0],p1_coord[1])   

# Electric field x and y components for second charge
E2_x=E_x(q2,p2_coord[0],p2_coord[1])   
E2_y=E_y(q2,p2_coord[0],p2_coord[1])

E_x_tot= E1_x + E2_x # Electric field total in x direction
E_y_tot= E1_y + E2_y # Electric field total in y direction

ax2.streamplot(x_coords, y_coords, E_x_tot, E_y_tot, density=2.0, linewidth=.9, arrowsize=.9)
#ax2.autoscale
ax2.set_title('The electric field of two charges, q1=1C and q2=-1C')
ax2.set_xlabel('x-axis (cm)')
ax2.set_ylabel('y-axis (cm)')
plt.show()






