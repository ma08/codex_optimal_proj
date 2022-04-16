

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

a.sort()
b.sort()

ans = 0
for i in range(n):
    ans += (a[i] * b[n - 1 - i]) % 998244353

print(ans % 998244353)
