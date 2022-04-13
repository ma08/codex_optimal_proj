import sys
import math

def main():
    gopher_x, gopher_y, dog_x, dog_y = [float(x) for x in sys.stdin.readline().split()]  # @UnusedVariable
    holes = []
    while True:
        hole = [float(x) for x in sys.stdin.readline().split()]
        if hole == []:
            break
        holes.append(hole)
    gopher_speed = math.sqrt((gopher_x-dog_x)**2 + (gopher_y-dog_y)**2)
    dog_speed = 2 * gopher_speed
    escape_hole = None
    for hole in holes:
        hole_speed = math.sqrt((hole[0]-dog_x)**2 + (hole[1]-dog_y)**2)
        if hole_speed < dog_speed:
            escape_hole = hole
    if escape_hole is None:
        print("The gopher cannot escape.")
    else:
        print("The gopher can escape through the hole at ({0:.3f},{1:.3f}).".format(escape_hole[0], escape_hole[1]))

if __name__ == '__main__':
    main()
