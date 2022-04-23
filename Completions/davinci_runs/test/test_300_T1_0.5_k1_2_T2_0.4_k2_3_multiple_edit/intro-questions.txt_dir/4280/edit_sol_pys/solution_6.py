
# TODO: Implement solution

#------------------------------------------------------------------------------#

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())

    edges = []
    for i in range(n - 1):
        edges.append(list(map(int, sys.stdin.readline().split())))

    print(solve(n, k, edges))

def solve(n, k, edges):
    pass

#------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()
