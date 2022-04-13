n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()
ans = 0
for i in range(n):
    ans += b[i] * (len(c) - bisect_right(c, b[i]))
    ans += a[i] * (len(c) - bisect_right(c, b[i]))
print(ans)
