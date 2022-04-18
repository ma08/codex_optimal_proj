
import math
import sys

def get_input():
    lines = sys.stdin.readlines()
    return [line.strip() for line in lines]

def get_spies_and_houses(input):
    spies = []
    houses = []
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char == 'S':
                spies.append((x, y))
            elif char == 'H':
                houses.append((x, y))
    return spies, houses

def manhattan_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def find_closest_house(spy, houses):
    closest_house = houses[0]
    closest_distance = manhattan_distance(spy, closest_house)
    for house in houses[1:]:
        distance = manhattan_distance(spy, house)
        if distance < closest_distance:
            closest_house = house
            closest_distance = distance
    return closest_house, closest_distance

def main():
    input = get_input()
    spies, houses = get_spies_and_houses(input)
    max_distance = 0
    for spy in spies:
        closest_house, closest_distance = find_closest_house(spy, houses)
        if closest_distance > max_distance:
            max_distance = closest_distance
    print(max_distance)

if __name__ == '__main__':
    main()
