

#------------------------------------------------------------------------------#

import sys

def main():
    n = int(sys.stdin.readline())

    edges = [0] * (n - 1)  # TODO: Change to appropriate data structure
    for i in range(n - 1):
        edges[i] = list(map(int, sys.stdin.readline().split()))  # TODO: Change to appropriate data structure

    print(solve(n, edges))

def solve(n, edges):
    # TODO: Implement solution
    pass

#------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()
