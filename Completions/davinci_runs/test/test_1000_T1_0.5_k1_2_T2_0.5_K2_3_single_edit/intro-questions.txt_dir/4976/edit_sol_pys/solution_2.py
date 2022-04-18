
from sys import stdin
from math import hypot

def main():
    gopher_x, gopher_y, dog_x, dog_y = map(float, stdin.readline().split())
    for line in stdin:
        hole_x, hole_y = map(float, line.split()) 
        gopher_distance = hypot(gopher_x - hole_x, gopher_y - hole_y)
        dog_distance = hypot(dog_x - hole_x, dog_y - hole_y)
        if gopher_distance <= dog_distance / 2:
            print("The gopher can escape through the hole at ({:.3f},{:.3f}).".format(hole_x, hole_y))
            return
    print("The gopher cannot escape.")

if __name__ == '__main__':
    main()
