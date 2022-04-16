
lines = []
r, c, zr, zc = map(int, input().split())

for i in range(r):
    lines.append(input())
for i in range(r):
    for k in range(zr):
        for j in range(c):
            for l in range(zc):
                print(lines[i][j], end='')
        print()
