
r, c, zr, zc = map(int, input().split())

for i in range(r):
    line = list(input())
    for k in range(zr):
        for j in line:
            for l in range(zc - 1):
                print(j, end='')
            print(j)
