
import sys
import math

def main():
    # Read input
    M, N = [int(x) for x in sys.stdin.readline().strip().split()]
    T = [int(x) for x in sys.stdin.readline().strip().split()]
    X = [int(x) for x in sys.stdin.readline().strip().split()]

    # Calculate the differences in time and space
    time_diff = [T[i+1]-T[i] for i in range(len(T)-1)]
    space_diff = [X[i+1]-X[i] for i in range(len(X)-1)]

    # Calculate the possible speeds
    speeds = sorted(set(time_diff[i]/space_diff[i] for i in range(len(time_diff))))
    print(len(speeds))
    print(*speeds, sep=' ')

if __name__ == "__main__":
    main()
