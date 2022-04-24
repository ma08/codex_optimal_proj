import math

def main():
    """
    We start with the first point and move towards the last point.
    For each point, we check that there are points at a distance of 2^1, 2^2, 2^3, ..., 2^log2(10^9)
    """
    n = int(input())
    points = list(map(int, input().split()))

    def is_pow_of_2(x):
        """
        Check that the given number is a power of 2
        """
        return int(math.log2(x)) == math.log2(x)

    points.sort() # Sort points to make sure that points are in ascending order
    max_points = [] # List of points that satisfy the given condition
    for point_idx in range(n):
        point = points[point_idx]
        temp_max_points = [point] # List of points that satisfy the given condition for a particular point
        for pow_idx in range(1, int(math.log2(10**9))):
            # We check that there are points at a distance of 2^1, 2^2, 2^3, ..., 2^log2(10^9)
            if (point + 2**pow_idx in points) and (point - 2**pow_idx in points):
                temp_max_points.append(point + 2**pow_idx)
                temp_max_points.append(point - 2**pow_idx)
            else:
                break
        if len(temp_max_points) > len(max_points):
            # If there are more points that satisfy the given condition for the current point than for the previous points
            # then we set the current points as the maximum points
            max_points = temp_max_points

    max_points.sort() # Sort points to make sure that points are in ascending order

    print(len(max_points))
    print(*max_points)

if __name__ == "__main__":
    main()
