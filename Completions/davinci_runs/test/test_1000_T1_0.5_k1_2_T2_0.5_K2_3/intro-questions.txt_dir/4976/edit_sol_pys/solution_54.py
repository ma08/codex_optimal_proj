#!/usr/bin/env python3


from sys import stdin
from math import hypot

def main():
    gopher_x, gopher_y, dog_x, dog_y = map(float, stdin.readline().split()) # read all four values in one line
    for line in stdin:
        hole_x, hole_y = map(float, line.split()) # read the two values on one line
        gopher_distance = hypot(gopher_x - hole_x, gopher_y - hole_y) # calculate the distance from the gopher to the hole
        dog_distance = hypot(dog_x - hole_x, dog_y - hole_y) # calculate the distance from the dog to the hole
        if gopher_distance <= dog_distance / 2: # the gopher can escape if it is closer to the hole than the dog is
            print("The gopher can escape through the hole at ({:.3f}, {:.3f}).".format(hole_x, hole_y)) # print the coordinates of the hole
            return
    print("The gopher cannot escape.")

if __name__ == '__main__':
    main() # run the main function
