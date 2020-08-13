# Random walk in two dimensions

import random
import numpy as np
import pylab 

def plot_walk(x,y):
    
    pylab.title('Random Walk simulations')
    pylab.plot(x,y)
    pylab.show()

def distance(x,y):
    x_f = x[-1]
    y_f = y[-1]

    d = (x_f**2 + y_f**2)**0.5
    return d

def walk_2D(steps):

    x = [0]
    y = [0]
    route = [0,0]

    for i in range(steps):

        walk = random.choice([[0,1],[0,-1],[1,0],[-1,0]])
#        print('paso',walk)
 
        sum_vec = np.array(route) + np.array(walk)
        route = sum_vec
        print(route)
        x.append(route[0])
        y.append(route[1])

        #print(route)
    plot_walk(x,y)

    print('Distancia final: ', distance(x,y))
    


if __name__ == '__main__':
    steps = 10000
    walk_2D(steps)
