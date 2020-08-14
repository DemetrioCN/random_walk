# Random Walk in One Dimension

# DemetrioCN

import random

# Choose the next step and add it to the previous one
def walk_1D(steps):

    count = 0
    for i in range(steps):
        walk = random.choice([(1),(-1)])
        count += walk

    return count


# Compute the distance from 0
def random_walk_1D(steps, attempts):
    distance_sqrt = 0

    for attempt in range(attempts):
        distance = walk_1D(steps)
        distance_sqrt += distance**2

    average_distance = (distance_sqrt/attempts)**0.5
    return round(average_distance,2)


def main(steps_list, attempts):
    print("\n")
    print(10*"-","RandomWalk's distances in One Dimension" ,10*"-")
    print("\n")

    print(f'Number of attempts: ', attempts)

    print("\n")

    for i in steps_list:
        d = random_walk_1D(i,attempts)
        print(f'The final distance for {i} steps is {d}')

    print("\n")


# Program entry
if __name__ == '__main__':
    steps_list = [100,200,300,400,500]
    attempts = 10000
    
    main(steps_list, attempts)


