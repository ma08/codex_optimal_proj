# -*- coding: utf-8 -*-

import sys

def main():
    n, t = map(int, input().split())
    min_cost = t + 1 # 入力例2のようにTLEになる場合を考慮
    for _ in range(n):
        cost, time = map(int, input().split())
        if time <= t:
            min_cost = min(min_cost, cost)
    if min_cost > t:
        print("TLE")
    else:
        print(min_cost)

if __name__ == "__main__":
    main()
