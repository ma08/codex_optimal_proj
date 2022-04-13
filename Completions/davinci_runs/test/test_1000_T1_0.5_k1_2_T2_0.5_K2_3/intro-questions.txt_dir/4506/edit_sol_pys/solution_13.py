
n = int(input())
a = list(map(int, input().split()))[:n]
b = list(map(int, input().split()))[:n]
a.sort()
b.sort(reverse=True)
ans = 0
for i in range(n):
    ans += (a[i] * b[i]) % 998244353
print(ans % 998244353)
