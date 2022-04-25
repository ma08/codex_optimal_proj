

#------------------------------------------------------------------------------#

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())

    xs = [0] * n
    for i in range(n):
        xs[i] = list(map(int, sys.stdin.readline().split()))

    print(solve(n, k, xs))

def solve(n, k, xs):
    # TODO: Implement solution
    pass

#------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()
