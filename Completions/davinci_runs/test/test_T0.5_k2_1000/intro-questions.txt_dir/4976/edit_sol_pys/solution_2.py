

import sys
import math

def escape(goat, wolf, holes):
    if goat == wolf:
        return "The goat cannot escape."

    goat_speed = math.sqrt(sum([(goat[i] - wolf[i])**2 for i in range(len(goat))]))
    wolf_speed = 2*goat_speed

    for hole in holes:
        hole_distance = math.sqrt(sum([(goat[i] - hole[i])**2 for i in range(len(goat))]))
        wolf_distance = math.sqrt(sum([(wolf[i] - hole[i])**2 for i in range(len(wolf))]))

        if hole_distance/goat_speed < wolf_distance/wolf_speed:
            return "The goat can escape through the hole at ({0:.3f},{1:.3f}).".format(hole[0], hole[1])

    return "The goat cannot escape."


def main():
    goat = [float(x) for x in input().split()]
    wolf = [float(x) for x in input().split()]
    holes = []

    for line in sys.stdin.readlines():
        holes.append([float(x) for x in line.split()])

    print(escape(goat, wolf, holes))

if __name__ == '__main__':
    main()
