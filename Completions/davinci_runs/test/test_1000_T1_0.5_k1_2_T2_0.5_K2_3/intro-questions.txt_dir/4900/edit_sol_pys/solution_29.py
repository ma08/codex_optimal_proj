#!/usr/bin/python3

import sys

def main():
    n = int(sys.stdin.readline())
    distances = []
    for i in range(n):
        distances.append(list(map(int, sys.stdin.readline().split())))
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
    for i in range(n - 1):
        for j in range(i + 1, n):
            if distances[i][j] == 1 and distances[i][j] == distances[j][i]:
                print(str(i + 1) + " " + str(j + 1))

main()
