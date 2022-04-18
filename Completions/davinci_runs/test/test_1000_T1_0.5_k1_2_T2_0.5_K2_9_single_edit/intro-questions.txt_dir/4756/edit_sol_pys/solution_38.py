

import sys

def main():
    # Read input and remove newline character
    num_citizens = int(sys.stdin.readline().strip())
    coordinates = [tuple(map(int, line.split())) for line in sys.stdin.readlines()]

    # Find the minimum and maximum x and y coordinates
    min_x, max_x = float("inf"), float("-inf")
    min_y, max_y = float("inf"), float("-inf")
    for x, y in coordinates:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    # Check if the citizens are perfectly aligned
    if min_x == max_x or min_y == max_y:
        print(0)
        return
    
    # Calculate the y-intercept of the line
    intercept = max_y - ((max_y - min_y) / (max_x - min_x)) * max_x

    # Print the result
    print(intercept)

if __name__ == "__main__":
    main()
