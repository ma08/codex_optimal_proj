import random

import sys

def get_input():
    return sys.stdin.read().splitlines()

def get_spies_and_houses(input_lines):
    spies = []
    houses = []
    for y, line in enumerate(input_lines):
        for x, char in enumerate(line):
            if char == 'S':
                spies.append((x, y))
            elif char == 'H':
                houses.append((x, y))
    return spies, houses

def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def find_closest_house(spy, house_set):
    return min(house_set, key=lambda house: manhattan_distance(spy, house))

def find_house_set(spies, houses):
    house_set = set()
    for spy in spies:
        closest_house = find_closest_house(spy, houses)
        house_set.add(closest_house)
    return house_set

def find_farthest_distance(spies, houses):
    house_set = find_house_set(spies, houses)
    return max(manhattan_distance(spy, find_closest_house(spy, house_set)) for spy in spies)

def main():
    input_lines = get_input()
    spies, houses = get_spies_and_houses(input_lines)
    farthest_distance = find_farthest_distance(spies, houses)
    print(farthest_distance)

if __name__ == '__main__':
    main()
