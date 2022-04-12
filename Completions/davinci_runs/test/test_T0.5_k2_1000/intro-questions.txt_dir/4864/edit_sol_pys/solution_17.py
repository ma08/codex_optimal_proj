r, c, zr, zc = map(int, input().split())

for i in range(r):
    line = input()
    for k in range(zr):  # repeat row
        for j in range(c):  # print each character
            for l in range(zc):  # repeat column
                print(line[j], end='')
        print()
