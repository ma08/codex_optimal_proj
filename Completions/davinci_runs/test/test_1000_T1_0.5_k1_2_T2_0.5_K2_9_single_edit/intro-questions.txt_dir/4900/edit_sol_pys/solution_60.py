
import sys


def main():
    n, m = map(int, sys.stdin.readline().strip().split())
    distances = [[0 for i in range(n)] for j in range(n)]
    for i in range(m):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        distances[a - 1][b - 1] = c
        distances[b - 1][a - 1] = c
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    for i in range(n):
        for j in range(i + 1, n):
            if distances[i][j] > 1000000000:
                print(-1)
            else:
                print(distances[i][j])


main()
