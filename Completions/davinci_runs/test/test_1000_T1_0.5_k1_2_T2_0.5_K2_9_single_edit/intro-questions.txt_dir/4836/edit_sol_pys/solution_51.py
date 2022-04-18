

import sys

def main():
    N, C = map(int, sys.stdin.readline().split())
    weights = list(map(int, sys.stdin.readline().split()))
    weights.sort()
    eaten = 0
    for i in range(N):
        if weights[i] <= C:
            C -= weights[i]
            eaten += 1
    print eaten

main()
