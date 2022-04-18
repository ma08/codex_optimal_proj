

import sys

def main():
    N, C = [int(i) for i in sys.stdin.readline().split()]
    weights = [int(i) for i in sys.stdin.readline().split()]
    weights.sort()
    eaten = 0 
    for i in range(N):
        if weights[i] <= C:
            C -= weights[i]
            eaten += 1
    print eaten

main()
