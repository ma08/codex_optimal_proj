
import sys

def main():
    n = int(sys.stdin.readline())
    villages = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
    roads = []
    for i in range(1, n):
        roads.append((i, i+1))
        villages[i-1][i] = 0
        villages[i][i-1] = 0
    for i in range(1, n):
        for j in range(i+2, n):
            if villages[i-1][j-1] == villages[i-1][0] + villages[0][j-1]:
                roads.append((i, j))
                villages[i-1][j-1] = 0
                villages[j-1][i-1] = 0
    for road in roads:
        print(road[0], road[1], sep=' ')

if __name__ == '__main__':
    main()
