import sys
import math

def main():
    n, t = map(int, sys.stdin.readline().split())
    if n == 1:
        print(0)
        return
    min_cost = t + 1
    for _ in range(n):
        cost, time = map(int, sys.stdin.readline().split())
        if time <= t:
            min_cost = min(min_cost, cost)
    if min_cost == t + 1:
        print("TLE")
    else:
        print(min_cost)

if __name__ == "__main__":
    main()
