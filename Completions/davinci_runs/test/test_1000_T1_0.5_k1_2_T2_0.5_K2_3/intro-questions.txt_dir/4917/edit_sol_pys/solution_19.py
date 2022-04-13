
# program

n = int(input())

l = []

for i in range(n):
    l.append(list(map(int, input().split())))

l.sort(key=lambda x: x[1])

if l[0][1] >= l[1][0]:
    print("gunilla has a point")
else:
    print("edward is right")
