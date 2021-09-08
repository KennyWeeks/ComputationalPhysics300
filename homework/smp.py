#!/bin/bash
import matplotlib.pyplot as plt
import numpy as np

def simpson(start, end, parts, plot=1):
    #define the function
    f = lambda x: x**4 - 2*x + 1
    
    #define the X, Y points
    deltax = (end - start) / parts
    resultsx = np.linspace(start, end, parts+1)
    resultsy = f(resultsx)
    
    #-----------------------------------------------------
    #define the Simpson points and calculate the area here
    #-----------------------------------------------------
    area = []
    
    #This is a single line for loop for the lambda functions
    area = [((1/3)*deltax)*
    (f(start + (i*deltax)) + (4*(f(start + ((i + 1)*deltax)))) + f(start + ((i + 2) * deltax))) for i in range(0, parts - 2, 2)]

    #By default, we also output the plot.
    if plot==1:
        x = np.linspace(start,end,100)
        y = f(x)
        plt.plot(x, y, 'r')
        
        #-----------------------------------------------------
        #draw the curves based on Simpson points here
        #-----------------------------------------------------
    
        plt.xlim([start,end])
        plt.ylim([min(y),max(y)])
        plt.show()
    
    return sum(area)
    
if __name__ == "__main__":
    a = simpson(0, 2, 100)
    print(a)
    
    

