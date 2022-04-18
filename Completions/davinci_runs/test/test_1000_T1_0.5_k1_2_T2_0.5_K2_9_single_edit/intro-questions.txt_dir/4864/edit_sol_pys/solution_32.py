r, c, zr, zc = map(int, input().split())

for i in range(r):
    line = input()
    for k in range(zr):
        for j in range(c):
            for l in range(zc):
                print(line[j], end='')
        print()
