

import math

def escape(goat, dog, holes):
    if goat == dog:
        return "The goat cannot escape."

    goat_speed = math.sqrt(sum([(goat[i] - dog[i])**2 for i in range(len(goat))]))
    dog_speed = 2*goat_speed

    for hole in holes:
        hole_distance = math.sqrt(sum([(goat[i] - hole[i])**2 for i in range(len(goat))]))
        dog_distance = math.sqrt(sum([(dog[i] - hole[i])**2 for i in range(len(dog))]))

        if hole_distance/goat_speed < dog_distance/dog_speed:
            return "The goat can escape through the hole at ({0:.3f},{1:.3f}).".format(hole[0], hole[1])

    return "The gopher cannot escape."


def main():
    goat = [float(x) for x in input().split()]
    dog = [float(x) for x in input().split()]
    holes = []

    for line in sys.stdin.readlines():
        holes.append([float(x) for x in line.split()])

    print(escape(goat, dog, holes))

if __name__ == '__main__':
    main()
