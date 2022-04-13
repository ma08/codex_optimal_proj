#!/usr/bin/env python3

r, c, zr, zc = map(int, input().split())  # r = rows, c = columns, zr = zoom rows, zc = zoom columns

article = []
for i in range(r):
    article.append(input())

for i in range(r):
    for j in range(zr):
        for k in range(c):
            for l in range(zc):
                print(article[i][k], end="")
        print()
