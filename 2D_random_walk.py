# Random walk in two dimensions
# DemetrioCN

import random
import numpy as np
import pylab 


def distance(x,y):
    x_f = x[-1]
    y_f = y[-1]

    d = (x_f**2 + y_f**2)**0.5
    return d

def plot_walk(x,y):
    pylab.title('Random Walk simulation')
    pylab.plot(x,y)
    pylab.xlabel('x')
    pylab.ylabel('y')
    pylab.savefig('rand_walk_2D''.png', bbox_inches='tight', dpi=600)
    pylab.show()


def walk_2D(steps):
    x = [0]
    y = [0]
    route = [0,0]

    for i in range(steps):
        walk = random.choice([[0,1],[0,-1],[1,0],[-1,0]])
        sum_vec = np.array(route) + np.array(walk)
        route = sum_vec
        x.append(route[0])
        y.append(route[1])

        #print(route)
    plot_walk(x,y)

    print('Final distance: ', distance(x,y))
    print("\n")  
    
        

if __name__ == '__main__':
    print("\n")
    print(10*"-","Random Walk Simulation in 2D",10*"-")
    print("\n")

    steps = 10000
    walk_2D(steps)
