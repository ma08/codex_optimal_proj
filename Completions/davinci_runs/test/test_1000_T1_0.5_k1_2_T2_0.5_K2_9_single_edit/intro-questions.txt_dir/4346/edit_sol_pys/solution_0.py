
import sys

def solve(L, v, l, r): # L = length of the road, v = speed, l = left, r = right
    if l == 1: # if the left side is 1, it means that the left side is the starting point
        return (L - r) // v + 1 # calculate the number of the whole road divided by speed
    else:
        return (L - r) // v + (l - 1) // v

if __name__ == "__main__":
    t = int(raw_input())
    for _ in range(t):
        L, v, l, r = map(int, raw_input().split())
        print solve(L, v, l, r)
