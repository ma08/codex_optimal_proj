

import sys
import math

def readline():
    return sys.stdin.readline()

def main():
    gopher_x, gopher_y, dog_x, dog_y = [float(n) for n in readline().split()]  # read the gopher and dog position
    gopher_speed = math.sqrt((dog_x - gopher_x)**2 + (dog_y - gopher_y)**2)  # calculate the gopher speed
    dog_speed = 2 * gopher_speed  # calculate the dog speed
    hole_found = False
    while True:
        hole_x, hole_y = [float(n) for n in readline().split()]  # read the hole position
        gopher_time = math.sqrt((hole_x - gopher_x)**2 + (hole_y - gopher_y)**2) / gopher_speed  # calculate the time the gopher needs to reach the hole
        dog_time = math.sqrt((hole_x - dog_x)**2 + (hole_y - dog_y)**2) / dog_speed  # calculate the time the dog needs to reach the hole
        if gopher_time < dog_time:  # compare the times and see if the gopher can escape
            print "The gopher can escape through the hole at ({:.3f},{:.3f}).".format(hole_x, hole_y)
            hole_found = True
            break
    if not hole_found:
        print "The gopher cannot escape."

if __name__ == '__main__':
    main()
