import sys
input = sys.stdin.readline


n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

a.sort()
b.sort()
c.sort()

ans = 0
for i in range(n):
    x = a[i]
    y = bisect.bisect_left(b,x)
    z = bisect.bisect_right(c,x)
    ans += y*(m-z)

print(ans)
