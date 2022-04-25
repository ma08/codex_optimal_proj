import sys
n = int(sys.stdin.readline())
l = []
for i in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

x = int(sys.stdin.readline())
for i in range(n):
    if x in l[i]:
        print(i + 1, l[i].index(x) + 1)
        break
