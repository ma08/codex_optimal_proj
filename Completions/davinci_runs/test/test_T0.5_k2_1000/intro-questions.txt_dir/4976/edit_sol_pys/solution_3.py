
import sys
import math

def readline():
    return sys.stdin.readline()

def main():
    gopher_x, gopher_y, dog_x, dog_y = [float(n) for n in readline().split()]  # gopher's position and dog's position
    gopher_speed = math.sqrt((dog_x - gopher_x)**2 + (dog_y - gopher_y)**2)  # gopher's speed
    dog_speed = 2 * gopher_speed  # dog's speed
    hole_found = False
    while True:
        hole_x, hole_y = [float(n) for n in readline().split()]
        gopher_time = math.sqrt((hole_x - gopher_x)**2 + (hole_y - gopher_y)**2) / gopher_speed  # time for gopher to reach the hole
        dog_time = math.sqrt((hole_x - dog_x)**2 + (hole_y - dog_y)**2) / dog_speed
        if gopher_time < dog_time:
            print "The gopher can escape through the hole at ({:.3f},{:.3f}).".format(hole_x, hole_y)
            hole_found = True
            break
    if not hole_found:
        print "The gopher cannot escape."

if __name__ == '__main__':
    main()
