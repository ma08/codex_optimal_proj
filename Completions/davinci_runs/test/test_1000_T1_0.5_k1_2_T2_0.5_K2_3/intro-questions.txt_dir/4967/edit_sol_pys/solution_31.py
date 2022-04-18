
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
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            block = grid[row][column]
            if block == 'H':
                safe_houses.append((column, row))
    return safe_houses

def get_spies(grid):
    """
    Returns a list of coordinates of spies.
    """
    spies = []
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            block = grid[row][column]
            if block == 'S':
                spies.append((column, row))
    return spies

def get_manhattan_distance(coord1, coord2):
    """
    Returns the manhattan distance between two coordinates.
    """
    x1, y1 = coord1[0], coord1[1]
    x2, y2 = coord2[0], coord2[1]
    return abs(x1 - x2) + abs(y1 - y2) - 1

def get_nearest_safe_house(spy, safe_houses):
    """
    Returns the nearest safe house to a spy and the distance to it.
    """
    distances = {}
    for safe_house in safe_houses:
        distances[safe_house] = get_manhattan_distance(spy, safe_house)
    nearest_safe_house = min(distances, key=distances.get)
    return distances[nearest_safe_house]

def get_max_distance(grid, safe_houses, spies):
    """
    Returns the maximum manhattan distance a spy has to travel to reach the nearest safe house.
    """
    max_distance = 0
    for spy in spies:
        distance = get_nearest_safe_house(spy, safe_houses)
        if distance > max_distance:
            max_distance = distance
    return max_distance

def main():
    grid = get_input()
    safe_houses = get_safe_houses(grid)
    spies = get_spies(grid)
    max_distance = get_max_distance(grid, safe_houses, spies)
    print(max_distance)

if __name__ == '__main__':
    main()
