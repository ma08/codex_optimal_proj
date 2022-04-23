
# TODO: Implement solution

#------------------------------------------------------------------------------#

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())

    edges = [[] for _ in range(n - 1)]
    for i in range(n - 1):
        edges[i] = list(map(int, sys.stdin.readline().split()))

    print(solve(n, k, edges))

def solve(n, k, edges):
    pass

#------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()
