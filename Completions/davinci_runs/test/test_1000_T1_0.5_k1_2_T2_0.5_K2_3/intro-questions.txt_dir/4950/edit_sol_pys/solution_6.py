
#
import sys

def main():
    n = int(sys.stdin.readline().strip())  # number of segments
    road = []  # list of segments

    for i in range(n):
        t, d = map(int, sys.stdin.readline().strip().split())
        road.append((t, d))

    max_speed = 0
    for i in range(1, n):
        max_speed = max(max_speed, (road[i][1] - road[i - 1][1]) / (road[i][0] - road[i - 1][0]))

    print(int(max_speed))

if __name__ == '__main__':
    main()
