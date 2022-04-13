
import sys

def main():
    N, C = map(int, sys.stdin.readline().split()) # N = number of cookies, C = capacity of jar
    weights = map(int, sys.stdin.readline().split()) # weights of cookies
    weights.sort()
    eaten = 0 # number of cookies eaten
    for i in range(N):
        if weights[i] <= C:
            C -= weights[i]
            eaten += 1
    print eaten

main()
