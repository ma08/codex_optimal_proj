
import sys
import math

def escape(gopher, dog, holes):
    if gopher == dog:
        return "The gopher cannot escape."

    gopher_speed = math.sqrt(sum([(gopher[i] - dog[i])**2 for i in range(len(dog))]))
    dog_speed = 2*gopher_speed

    for hole in holes:
        hole_distance = math.sqrt(sum([(gopher[i] - hole[i])**2 for i in range(len(dog))]))
        dog_distance = math.sqrt(sum([(dog[i] - hole[i])**2 for i in range(len(dog))]))

        if hole_distance/gopher_speed < dog_distance/dog_speed:
            return "The gopher can escape through the hole at ({0:.3f},{1:.3f}).".format(hole[0], hole[1])

    return "The gopher cannot escape."


def main():
    line = sys.stdin.readline()
    gopher = [float(x) for x in line.split()]
    line = sys.stdin.readline()
    dog = [float(x) for x in line.split()]
    holes = []

    for line in sys.stdin.readlines():
        holes.append([float(x) for x in line.split()])

    print(escape(gopher, dog, holes))

if __name__ == '__main__':
    main()
