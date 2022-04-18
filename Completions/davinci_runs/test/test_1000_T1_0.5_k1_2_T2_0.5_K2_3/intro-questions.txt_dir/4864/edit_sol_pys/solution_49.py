
r, c, zr, zc = map(int, input().split()) 

for i in range(r):
    lines = input()
    for k in range(zr):
        for j in range(c):
            for l in range(zc):
                print(lines[j], end='')
        print()
