

import sys
import math

def main():
    # Read input
    M, N = [int(x) for x in sys.stdin.readline().strip().split()]
    T = [int(x) for x in sys.stdin.readline().strip().split()]
    X = [int(x) for x in sys.stdin.readline().strip().split()]

    # Calculate the differences in time and distance
    time_diff = [T[i+1]-T[i] for i in range(len(T)-1)] # [1, 1, 1, 1]
    distance_diff = [X[i+1]-X[i] for i in range(len(X)-1)] # [1, 1, 1, 1]

    # Calculate the possible speeds
    speeds = sorted(set(time_diff[i]/distance_diff[i] for i in range(len(time_diff)))) # [1.0]
    print(len(speeds))
    print(*speeds)

if __name__ == "__main__":
    main()
