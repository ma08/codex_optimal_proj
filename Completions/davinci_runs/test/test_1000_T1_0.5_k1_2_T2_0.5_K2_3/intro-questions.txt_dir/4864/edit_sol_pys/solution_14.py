

r, c, zr, zc = map(int, input().split())
lines = []


for i in range(r):
    lines.append(input())

for line in lines:
    for k in range(zr):
        for j in range(len(line)):
            for l in range(zc-1):

                print(line[j], end="")

        print(line[j])
