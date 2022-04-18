import math


n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += a[i]*(i+1)*(n-i)

print(ans)
