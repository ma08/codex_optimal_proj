
x1, x2, x3, x4, x5 = map(int, input().split())
for i in range(1, 6):
    if eval('x'+str(i)) == 0:
        print(i)
