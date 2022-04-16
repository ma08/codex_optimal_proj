

import sys

def main():
    n = int(input())
    road = [0] * n

    for i in range(n - 1):
        t, d = map(int, input().split())
        road[i] = (d - road[i - 1]) / (t - i)

    max_speed = max(road)

    print(int(max_speed))

if __name__ == '__main__':
    main()
