

from collections import defaultdict

def get_city_roads(roads):
    city_roads = defaultdict(list)
    for road in roads:
        city_roads[road[0]].append(road[1])
        city_roads[road[1]].append(road[0])
    return city_roads

def get_city_cost(roads, city_roads):
    city_cost = defaultdict(int)
    for road in roads:
        city_cost[road[0]] += road[2]
        city_cost[road[1]] += road[2]
    return city_cost
import sys

def main():
    n, m, k = [int(x) for x in sys.stdin.readline().split()]
    roads = [[int(x) for x in sys.stdin.readline().split()] for _ in range(m)] # [from, to, cost]
    city_roads = get_city_roads(roads)
    city_cost = get_city_cost(roads, city_roads)
    print(city_roads)
    print(city_cost)

if __name__ == "__main__":
    main()
