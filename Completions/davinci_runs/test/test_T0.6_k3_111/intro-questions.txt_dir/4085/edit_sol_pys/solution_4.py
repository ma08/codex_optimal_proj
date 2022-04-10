
n = int(input())

d = [int(x) for x in input().split()]
d.sort()
if n == 1:
    print(max(d[0]*2, d[0]+1))
elif d[0] != 2:
    print(-1)
elif d[n-1]%2 == 0:
    print(d[n-1])
else:
    print(-1)
