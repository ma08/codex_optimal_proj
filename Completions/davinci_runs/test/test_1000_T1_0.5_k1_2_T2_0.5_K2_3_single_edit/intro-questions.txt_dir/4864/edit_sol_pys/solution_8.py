

r, c, zr, zc = map(int, input().split()) # r = rows, c = columns, zr = row zoom, zc = column zoom

for i in range(r):
    line = input()
    for j in range(zr):
        for k in range(c):
            for l in range(zc):
                print(line[k], end='')
        print()
