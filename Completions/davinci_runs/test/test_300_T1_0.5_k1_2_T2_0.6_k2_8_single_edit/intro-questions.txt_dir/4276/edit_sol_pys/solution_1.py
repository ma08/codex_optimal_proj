
import sys

N, T = map(int, sys.stdin.readline().split())
min_cost = T + 1
for _ in range(N):
    cost, time = map(int, sys.stdin.readline().split())
    if time <= T:
        min_cost = min(min_cost, cost)
if min_cost > T:
    print("TLE")
else:
    print(min_cost)
