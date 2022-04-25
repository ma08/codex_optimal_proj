
#------------------------------------------------------------------------------#

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())

    edges = []
    for i in range(m):
        edges.append(list(map(int, sys.stdin.readline().split())))

    print(solve(n, m, edges))

def solve(n, m, edges):
    # TODO: Implement solution
    pass

#------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()
