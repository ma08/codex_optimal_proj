

n, t = map(int, input().split())
clist = []
for i in range(n):
    c, l = map(int, input().split())
    clist.append((c, l))

clist.sort()

for i in clist:
    if i[1] <= t:
        print(i[0])
        exit()
else:
    print("TLE")