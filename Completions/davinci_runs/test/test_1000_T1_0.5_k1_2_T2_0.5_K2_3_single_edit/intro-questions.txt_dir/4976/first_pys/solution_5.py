

import sys
from math import *

def distance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def main():
    data = sys.stdin.readlines()
    data = [tuple(map(float, line.split())) for line in data]
    
    gopher_x, gopher_y = data[0][0], data[0][1]
    dog_x, dog_y = data[0][2], data[0][3]
    holes = data[1:]

    for hole in holes:
        hole_x, hole_y = hole[0], hole[1]
        if distance(gopher_x, gopher_y, hole_x, hole_y) < distance(dog_x, dog_y, hole_x, hole_y):
            print("The gopher can escape through the hole at ({:.3f},{:.3f}).".format(hole_x, hole_y))
            return
    print("The gopher cannot escape.")

if __name__ == '__main__':
    main()