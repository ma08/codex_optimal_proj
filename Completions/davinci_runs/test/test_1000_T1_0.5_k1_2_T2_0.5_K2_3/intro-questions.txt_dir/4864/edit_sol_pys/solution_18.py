
lines = []
R, C, ZR, ZC = map(int, input().split())

for i in range(R):
    lines.append(input())
for line in lines:
    for i in range(ZR):
        for c in line:
            for j in range(ZC):
                print(c, end='')
        print('')
