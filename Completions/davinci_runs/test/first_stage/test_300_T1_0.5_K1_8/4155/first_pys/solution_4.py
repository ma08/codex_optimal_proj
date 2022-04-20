

import sys

# Read input
N = int(sys.stdin.readline())
h = [int(x) for x in sys.stdin.readline().split()]

# Find the maximum value in the h array
max_h = max(h)

# Initialize the number of watering operations
watering_ops = 0

# Keep watering until the maximum value is 0
while max_h > 0:
    # Initialize the start and end points of a watering operation
    start_point = -1
    end_point = -1

    # Iterate through the h array
    for i in range(N):
        # If the height of a flower is not 0
        if h[i] != 0:
            # If the start point is not initialized
            if start_point == -1:
                # Initialize the start point
                start_point = i
            # If the end point is not initialized
            if end_point == -1:
                # Initialize the end point
                end_point = i
            else:
                # If the height of the next flower is 0
                if h[i+1] == 0:
                    # Update the end point
                    end_point = i
                    # Water the flowers between the start point and end point
                    for j in range(start_point, end_point+1):
                        h[j] -= 1
                    # Update the number of watering operations
                    watering_ops += 1
                    # Reset the start and end points
                    start_point = -1
                    end_point = -1

    # If there is only one flower left
    if h[N-1] != 0:
        # Water the flower
        h[N-1] -= 1
        # Update the number of watering operations
        watering_ops += 1

    # Update the maximum value in the h array
    max_h = max(h)

# Print the result
print(watering_ops)