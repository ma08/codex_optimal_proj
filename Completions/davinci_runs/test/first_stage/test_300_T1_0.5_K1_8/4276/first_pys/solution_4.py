

import sys

n, t = map(int, sys.stdin.readline().split())

route_list = []
for i in range(n):
    c, t = map(int, sys.stdin.readline().split())
    route_list.append([c, t])

route_list = sorted(route_list, key=lambda x: x[1])

for route in route_list:
    if route[1] <= t:
        print(route[0])
        sys.exit()

print('TLE')