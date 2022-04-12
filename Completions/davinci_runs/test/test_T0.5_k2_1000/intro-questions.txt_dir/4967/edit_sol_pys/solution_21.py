
import sys

def get_input():
    """
    Reads input from stdin, parses lines into a list of lists.
    """
    input_list = []
    for line in sys.stdin:
        line = line.strip()
        input_list.append(list(line))
    return input_list

def get_safe_houses(grid):
    """
    Returns a list of coordinates of safe houses.
    """
    safe_houses = []
    for y, row in enumerate(grid):  # enumerate returns the index and the element
        for x, block in enumerate(row):  # enumerate returns the index and the element
            if block == 'H':
                safe_houses.append((x, y))
    return safe_houses

def get_spies(grid):
    """
    Returns a list of coordinates of spies.
    """
    spies = []
    for y, row in enumerate(grid):  # enumerate returns the index and the element
        for x, block in enumerate(row):  # enumerate returns the index and the element
            if block == 'S':
                spies.append((x, y))
    return spies

def get_manhattan_distance(coord1, coord2):
    """
    Returns the Manhattan distance between two coordinates.
    """
    x1, y1 = coord1  # unpack the tuple
    x2, y2 = coord2  # unpack the tuple
    return abs(x1 - x2) + abs(y1 - y2)

def get_nearest_safe_house(spy, safe_houses):
    """
    Returns the nearest safe house to a spy.
    """
    distances = {}
    for safe_house in safe_houses:
        distances[safe_house] = get_manhattan_distance(spy, safe_house)
    nearest_safe_house = min(distances, key=distances.get)  # get the key with the lowest value
    return distances[nearest_safe_house]  # return the value of the key

def get_max_distance(grid):
    """
    Returns the maximum Manhattan distance a spy has to travel to reach the nearest safe house.
    """
    safe_houses = get_safe_houses(grid)
    spies = get_spies(grid)
    max_distance = 0
    for spy in spies:
        distance = get_nearest_safe_house(spy, safe_houses)
        if distance > max_distance:
            max_distance = distance
    return max_distance

def main():
    grid = get_input()
    max_distance = get_max_distance(grid)
    print(max_distance)

if __name__ == '__main__':
    main()
