# ------------------------------------------------------------------------------#

import sys


def main():
    n, k = map(int, sys.stdin.readline().split())  # TODO: fix

    edges = [0] * (n - 1)
    for i in range(n - 1):
    # TODO: fix
        edges[i] = list(map(int, sys.stdin.readline().split()))

    print(solve(n, k, edges))

def solve(n, k, edges):
    # TODO: Implement solution
    pass

# ------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()
