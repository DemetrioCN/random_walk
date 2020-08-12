# Random Walk in one dimension
import random


def walk_1D(steps):

    count = 0
    for i in range(steps):
        walk = random.choice([(1),(-1)])
        count += walk
       # print(walk)
    return count



def random_walk_1D(steps, attempts):
    distance_sqrt = 0

    for attempt in range(attempts):
        distance = walk_1D(steps)
        distance_sqrt += distance**2
        #print('Final point: ',distance)    
        
    average_distance = (distance_sqrt/attempts)**0.5
    print("Average distance: ", round(average_distance,2))



if __name__ == '__main__':
    steps = 25
    attempts = 1000
    
    random_walk_1D(steps, attempts)



