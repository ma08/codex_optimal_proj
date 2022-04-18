

r, c, zr, zc = map(int, input().strip().split())

for i in range(r):
    line = input().strip()
    for j in range(zr):
        for k in range(c):
            for l in range(zc):
                print(line[k], end='')
        print("")
