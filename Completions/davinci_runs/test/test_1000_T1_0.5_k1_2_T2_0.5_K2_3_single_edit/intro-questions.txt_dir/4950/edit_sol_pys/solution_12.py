

import sys

def main():
    n = int(sys.stdin.readline().strip())
    road = []

    for i in range(n):
        x, y = map(int, sys.stdin.readline().strip().split())
        road.append((x, y))

    max_speed = 0
    for i in range(1, n):
        max_speed = max(max_speed, (road[i][1] - road[i - 1][1]) / (road[i][0] - road[i - 1][0]))

    print(int(max_speed))

if __name__ == '__main__':
    main()
