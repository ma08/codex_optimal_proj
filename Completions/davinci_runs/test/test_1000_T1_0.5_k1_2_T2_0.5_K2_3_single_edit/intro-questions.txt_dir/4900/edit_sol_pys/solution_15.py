
import sys

def main():
    n = int(sys.stdin.readline().strip())
    distances = []
    for i in range(n):
        distances.append(list(map(int, sys.stdin.readline().strip().split())))
        for j in range(i):
            if distances[i][j] == 0:
                distances[i][j] = distances[j][i]
        for j in range(i + 1, n):
            if distances[i][j] == 0:
                distances[i][j] = distances[i][j-1]
    for i in range(n - 1):
        for j in range(i + 1, n):
            for k in range(i + 1, j):
                if distances[i][k] + distances[k][j] == distances[i][j]:
                    print(i + 1, k + 1, j + 1)
                    exit()
    print(-1)

main()
