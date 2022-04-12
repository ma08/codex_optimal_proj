
import sys

def main():
    n = int(sys.stdin.readline())
    villages = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
    roads = []
    for i in range(1, n):
        roads.append((i, i+1))
        villages[i][i+1] = -1 # mark as used
        villages[i+1][i] = -1 # mark as used
    for i in range(1, n):
        for j in range(i+2, n):
            if villages[i][j] == villages[i][1] + villages[1][j]:
                roads.append((i, j))
                villages[j][i] = -1 # mark as used
    for road in roads:
        print(road[0], road[1])

if __name__ == '__main__':
    main()
