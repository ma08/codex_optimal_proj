

import math

def main():
    # Get input
    n, d = map(int, input().split())
    points = [list(map(int, input().split())) for _ in range(n)]

    # Calculate all possible distances
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            distances.append(math.sqrt(sum([(points[i][k] - points[j][k])**2 for k in range(d)])))

    # Count distances that are integers
    integer_count = 0
    for distance in distances:
        if distance == int(distance):
            integer_count += 1

    # Print result
    print(integer_count)

if __name__ == '__main__':
    main()