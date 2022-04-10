

import math

def get_hole_distance(gopher_x, gopher_y, hole_x, hole_y):
    return math.sqrt(math.pow(hole_x - gopher_x, 2) + math.pow(hole_y - gopher_y, 2))

def get_dog_distance(dog_x, dog_y, hole_x, hole_y):
    return math.sqrt(math.pow(hole_x - dog_x, 2) + math.pow(hole_y - dog_y, 2))

def main():
    gopher_x, gopher_y, dog_x, dog_y = map(float, input().split())

    hole_x, hole_y = map(float, input().split())
    min_gopher_distance = get_hole_distance(gopher_x, gopher_y, hole_x, hole_y)
    min_dog_distance = get_dog_distance(dog_x, dog_y, hole_x, hole_y)
    escape_hole = (hole_x, hole_y)

    while True:
        try:
            hole_x, hole_y = map(float, input().split())
        except ValueError:
            break

        gopher_distance = get_hole_distance(gopher_x, gopher_y, hole_x, hole_y)
        dog_distance = get_dog_distance(dog_x, dog_y, hole_x, hole_y)

        if gopher_distance < min_gopher_distance and dog_distance > min_dog_distance:
            min_gopher_distance = gopher_distance
            min_dog_distance = dog_distance
            escape_hole = (hole_x, hole_y)
        elif gopher_distance < min_gopher_distance and dog_distance < min_dog_distance:
            min_gopher_distance = gopher_distance
            min_dog_distance = dog_distance
            escape_hole = (hole_x, hole_y)

    if escape_hole == (hole_x, hole_y):
        print("The gopher cannot escape.")
    else:
        print("The gopher can escape through the hole at ({}, {}).".format(escape_hole[0], escape_hole[1]))

if __name__ == '__main__':
    main()