

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    from operator import itemgetter

    routes = []
    route_count = int(input())
    time = int(input())

    for i in range(route_count):
        route = list(map(int, input().split()))
        routes.append(route)

    routes = sorted(routes, key=itemgetter(1))

    for route in routes:
        if route[1] <= time:
            print(route[0])
            exit()

    print('TLE')