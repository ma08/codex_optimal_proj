
n = int(input())
a = list(map(int, input().split()))
a.sort()
b = list(map(int, input().split()))
b.sort()
c = list(map(int, input().split()))
c.sort()
ans = 0
for i in range(n):
    ans += b[i] * c[i]
print(ans)
