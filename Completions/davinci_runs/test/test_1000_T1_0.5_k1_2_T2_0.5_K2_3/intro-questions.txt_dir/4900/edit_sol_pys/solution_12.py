#!/usr/bin/python3

import sys

def main():
    n = int(sys.stdin.readline().strip())
    p = int(sys.stdin.readline().strip())
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
    for i in range(p):
        a, b = map(int, sys.stdin.readline().strip().split())
        if distances[a - 1][b - 1] == 1:
            print('YES')
        else:
            print('NO')

main()
