
#!/usr/bin/env python3

#------------------------------------------------------------------------------#

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())

    edges = [0] * (n - 1) # 0-indexed
    for i in range(n - 1): # 0-indexed
        edges[i] = list(map(int, sys.stdin.readline().split())) # 0-indexed

    print(solve(n, k, edges))

def solve(n, k, edges):
    return 0

#------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()
