

#------------------------------------------------------------------------------#

import sys

def main():
    n = int(sys.stdin.readline())

    edges = [0] * (n - 1)
    for i in range(n - 1):
        edges[i] = list(map(int, sys.stdin.readline().split()))

    print(solve(n, edges))

def solve(n, edges):
    # TODO: Implement solution
    return 0

#------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()
