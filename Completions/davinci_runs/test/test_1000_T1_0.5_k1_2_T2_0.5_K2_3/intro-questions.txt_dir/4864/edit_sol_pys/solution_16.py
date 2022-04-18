r, c, zr, zc = map(int, input().split())
line = []
for i in range(r):
    line.append(input())

for i in line:
    for j in range(zr):
        for k in i:
            for l in range(zc):
                print(k, end='')
        print('')
