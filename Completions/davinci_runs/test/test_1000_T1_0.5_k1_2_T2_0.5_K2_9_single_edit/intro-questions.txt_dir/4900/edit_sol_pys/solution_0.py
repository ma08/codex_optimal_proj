
import sys

def main():
    n = int(sys.stdin.readline().strip())
    distances = []
    for i in range(n):
        distances.append(list(map(int, sys.stdin.readline().strip().split())))
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
    result = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if distances[i - 1][j - 1] == 1:
                result.append((i, j))
    result.sort()
    print(len(result))
    for r in result:
        print(r[0], r[1])

main()
