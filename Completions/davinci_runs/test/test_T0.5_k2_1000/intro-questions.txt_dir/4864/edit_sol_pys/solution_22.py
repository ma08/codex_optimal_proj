r, c, zr, zc = map(int, input().split())

for i in range(r):
    line = list(input())
    for k in range(zr):
        for j in range(len(line)):
            for l in range(zc):
                print(line[j], end="")
        print()
