
lines = []
r, c, zr, zc = map(int, input().split())

for i in range(r):
    lines.append(input())
for line in lines:
    for j in range(zr):
        for k in range(c):
            for l in range(zc):
                print(line[k], end='')
        print()
