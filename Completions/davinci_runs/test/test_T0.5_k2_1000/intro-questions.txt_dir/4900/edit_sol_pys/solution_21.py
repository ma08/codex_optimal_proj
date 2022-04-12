import sys

def main():
    n = int(sys.stdin.readline().strip())
    distances = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        distances[i] = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(n):
        for j in range(n):
            if i == j:
                distances[i][j] = 0
            elif distances[i][j] == 0:
                distances[i][j] = distances[j][i]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                distances[j][k] = min(distances[j][k], distances[j][i] + distances[i][k])
    for i in range(n):
        for j in range(n):
            if distances[i][j] == 1:
                print(i + 1, j + 1)

main()
