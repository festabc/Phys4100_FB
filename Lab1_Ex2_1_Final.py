import sys

import numpy as np

def calc_t():
    
    if sys.argv[1] == '-height' and sys.argv[3] =='-time' :
        h = float(sys.argv[2])
        t = float(sys.argv[4])
        
    elif sys.argv[1] == '-time' and sys.argv[3] =='-height' :
        t = float(sys.argv[2])
        h = float(sys.argv[4])
        
#     h=float(input('What is the height of the tower (in meters): ',))
    while h<=0:
        h=float(input('Error, height of the tower cannot be 0 or smaller than 0. Please enter another value: ',))
    

#     t=float(input('Time, for how long has the ball been falling (in seconds): ',))
    while t<=0:
        t=float(input('Error, time cannot be 0 or smaller than 0. Please enter another value: ',))
        
    
    t_max=np.sqrt(2*h/9.8)
    if t>t_max:
        print('This ball has long ago fallen to the ground (at time {} seconds)'.format(t_max))
    
    else: 
        delta_h=(0.5)*(9.8)*(t**2) #delta_h=h(tower)-h(ball at given time)
        
        h_ball=h-delta_h
        
        
        print('Current height of the ball is {} meters above the ground.'.format(h_ball))
        

if __name__=="__main__":

     calc_t()

     