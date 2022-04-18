from sys import stdout

r, c, zr, zc = map(int, input().split())

for i in range(r):
    line = input()
    for k in range(zr):
        for j in range(c):
            for l in range(zc):
                stdout.write(line[j])
        print()
