
import sys

r, c, zr, zc = map(int, sys.stdin.readline().split())

for i in range(r):
    line = sys.stdin.readline()
    for j in range(zr):
        for k in range(c):
            for l in range(zc):
                print(line[k], end='')
        print("")
