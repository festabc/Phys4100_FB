## Excercise 2.4

## A spaceship travels from Earth in a straight line at relativistic speed v to another planet x light years away. Write a program to ask the user for the value of x and the speed v as a fraction of the speed of light c, then print out the time in years that the spaceship takes to reach its destination (a) in the rest frame of an observer on Earth and (b) as perceived by a passenger on board the ship. Use your program to calculate the answers for a planet 10 light years away with v = 0.99c.


import numpy as np
import argparse

def calc_t():
    
    parser=argparse.ArgumentParser()
    
    #Required parameters
    parser.add_argument("-distance", type=float, help="the distance to the unknown planet, in light years")
    parser.add_argument("-velocity", type=float, help="velocity of the spaceship, as a fraction of the speed of light")
    
    args=parser.parse_args()
    print(args)
    
    #speed of light in m/s
    c=3e8 
    
   
    # x is the distance to the unknown planet in light years, in the spaceship's frame of reference
    x=args.distance #float(input('What is the distance to the unkown planet, in light years? '),)
    print(x)
    while x<=0:
        x=float(input('Error! Distance cannot be 0 or smaller than 0. Please enter another value:  ' ,))
    
    
    # v is the speed of spaceship as a fraction of the speed of light
    v=args.velocity  #float(input('What is the speed of the spaceship as a fraction of the speed of light? ' ,))
    while v<=0:
        v=float(input('''The speed of the spaceship cannot be 0 and it cannot be negative as the spaceship
        is travelling away from Earth to the unknown planet, and not towards it. Please enter another value: ''' ,))
    while v>=1:
        v=float(input('''The speed of the spaceship cannot be larger than speed of light.  Please enter another value <1  ''' ,))
        
    
    beta=np.sqrt(1-v**2) # v is a fraction of c already, so no need to use v/c
    
    gamma=1/beta
    
    v_m=v*c       # v, speed in m/s
    x_m=x*9.5e15    # conversion of x, distance from light years to m
    
    # Time in the spaceship's frame of reference
    proper_time_s=x_m/v_m    # spaceship's time in s   
    
    proper_time_y=proper_time_s*3.15e-7  # spaceship's time in years
    

    # Time in the Earth's frame of reference
    observer_time=gamma*proper_time_y   # time for the observer on Earth, in years
    
    
    print('''a) The time it takes for the spaceship to reach its destination in the rest frame of 
    an observer on Earth is {} years.'''.format(round(observer_time, 2)))
    print('''b) The time it takes for the spaceship to reach its destination, 
    as percieved by a passanger onboard, is {} years.'''.format(round(proper_time_y, 2)))


if __name__=="__main__":
    calc_t()

    