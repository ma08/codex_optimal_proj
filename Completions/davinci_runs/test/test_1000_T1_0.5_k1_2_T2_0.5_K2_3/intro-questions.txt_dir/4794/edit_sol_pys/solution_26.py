#!/usr/bin/env python3

def main():
    r, c = map(int, input().split())
    l = []
    for i in range(r):
        l.append(input())
    d = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    for i in range(r - 1):
        for j in range(c - 1):
            if l[i][j] == '.' and l[i][j + 1] == '.' and l[i + 1][j] == '.' and l[i + 1][j + 1] == '.':
                d[0] += 1
            elif l[i][j] == 'X' and l[i][j+1] == '.' and l[i+1][j] == '.' and l[i+1][j+1] == '.':
                d[1] += 1
            elif l[i][j] == '.' and l[i][j+1] == 'X' and l[i+1][j] == '.' and l[i+1][j+1] == '.':
                d[1] += 1
            elif l[i][j] == '.' and l[i][j+1] == '.' and l[i+1][j] == 'X' and l[i+1][j+1] == '.':
                d[1] += 1
            elif l[i][j] == '.' and l[i][j+1] == '.' and l[i+1][j] == '.' and l[i+1][j+1] == 'X':
                d[1] += 1
            elif l[i][j] == 'X' and l[i][j+1] == 'X' and l[i+1][j] == '.' and l[i+1][j+1] == '.':
                d[2] += 1
            elif l[i][j] == 'X' and l[i][j+1] == '.' and l[i+1][j] == 'X' and l[i+1][j+1] == '.':
                d[2] += 1
            elif l[i][j] == 'X' and l[i][j+1] == '.' and l[i+1][j] == '.' and l[i+1][j+1] == 'X':
                d[2] += 1
            elif l[i][j] == '.' and l[i][j+1] == 'X' and l[i+1][j] == 'X' and l[i+1][j+1] == '.':
                d[2] += 1
            elif l[i][j] == '.' and l[i][j+1] == 'X' and l[i+1][j] == '.' and l[i+1][j+1] == 'X':
                d[2] += 1
            elif l[i][j] == '.' and l[i][j+1] == '.' and l[i+1][j] == 'X' and l[i+1][j+1] == 'X':
                d[2] += 1
            elif l[i][j] == 'X' and l[i][j+1] == 'X' and l[i+1][j] == 'X' and l[i+1][j+1] == '.':
                d[3] += 1
            elif l[i][j] == 'X' and l[i][j+1] == 'X' and l[i+1][j] == '.' and l[i+1][j+1] == 'X':
                d[3] += 1
            elif l[i][j] == 'X' and l[i][j+1] == '.' and l[i+1][j] == 'X' and l[i+1][j+1] == 'X':
                d[3] += 1
            elif l[i][j] == '.' and l[i][j+1] == 'X' and l[i+1][j] == 'X' and l[i+1][j+1] == 'X':
                d[3] += 1
            elif l[i][j] == 'X' and l[i][j+1] == 'X' and l[i+1][j] == 'X' and l[i+1][j+1] == 'X':
                d[4] += 1
    for i in range(5):
        print(d[i])
main()
