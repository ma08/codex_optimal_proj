

R, C, ZR, ZC = map(int, input().split())

for i in range(R):
    line = input()
        print()
    for k in range(ZR):
        for j in range(C):
            for l in range(ZC):
                print(line[j], end='')
        print()
