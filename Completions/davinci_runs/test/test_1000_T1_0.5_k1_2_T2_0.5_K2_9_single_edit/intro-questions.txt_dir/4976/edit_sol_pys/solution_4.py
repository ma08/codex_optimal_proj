

import sys
import math

def gopher_escape(gopher, dog, hole)
    """
    Returns true if the gopher can escape through the hole, false otherwise.
    """
    # Compute the distance from the gopher to the hole
    gopher_to_hole = math.sqrt(math.pow(hole[0]-gopher[0],2) + math.pow(hole[1]-gopher[1],2))
    # Compute the distance from the dog to the hole
    dog_to_hole = math.sqrt(math.pow(hole[0]-dog[0],2) + math.pow(hole[1]-dog[1],2))
    # If the distance from the gopher to the hole is less than the distance from the dog to the hole, the gopher can escape
    return gopher_to_hole < dog_to_hole

def main()
    # Read the input
    gopher = [float(x) for x in sys.stdin.readline().strip().split()]
    dog = [float(x) for x in sys.stdin.readline().strip().split()]
    holes = []
    for line in sys.stdin:
        holes.append([float(x) for x in line.strip().split()])
    # Check if the gopher can escape through any of the holes
    for hole in holes:
        if gopher_escape(gopher, dog, hole):
            print('The gopher can escape through the hole at ({},{}).'.format(hole[0], hole[1]))
            return
    # If not, then the gopher cannot escape
    print('The gopher cannot escape.')

if __name__ == '__main__':
    main()
