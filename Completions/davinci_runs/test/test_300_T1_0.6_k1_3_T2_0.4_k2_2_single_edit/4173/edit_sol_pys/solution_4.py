
import sys

def solve(n, c_lib, c_road, cities):
    return 0

q = int(raw_input().strip())
for a0 in xrange(q):
    n, m, c_lib, c_road = raw_input().strip().split(' ')
    n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]
    cities = []
    for cities_i in xrange(m):
        cities_temp = map(int,raw_input().strip().split(' '))
        cities.append(cities_temp)
    print solve(n, c_lib, c_road, cities)
