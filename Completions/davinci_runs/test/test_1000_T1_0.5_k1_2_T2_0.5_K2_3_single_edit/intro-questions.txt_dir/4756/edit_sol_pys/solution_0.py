
import sys

def main():
    # Read input
    num_citizens = int(sys.stdin.readline())
    coordinates = [tuple(map(int, sys.stdin.readline().split())) for _ in range(num_citizens)]

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

    # Calculate the slope of the line
    slope = (max_y - min_y) / (max_x - min_x)

    # Calculate the y-intercept
    intercept = max_y - slope * max_x

    # Print the result
    print(intercept)

if __name__ == "__main__":
    main()
