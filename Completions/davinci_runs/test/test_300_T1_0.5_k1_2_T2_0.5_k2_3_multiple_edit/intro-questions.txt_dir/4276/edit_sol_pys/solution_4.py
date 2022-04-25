

import sys

def main():
    n, t = map(int, sys.stdin.readline().rstrip().split())
    min_cost = t + 1 # タイムリミット以上のものを入れておく
    for _ in range(n):
        cost, time = map(int, sys.stdin.readline().rstrip().split())
        print(cost, time)
        if time <= t:
            min_cost = min(min_cost, cost)
    if min_cost > t:
        print("TLE")
    else:
        print(min_cost)

if __name__ == "__main__":
    main()
