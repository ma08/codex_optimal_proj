mod = 998244353

def solve(n, a, b):
    a.sort()
    b.sort()
    ans = 0
    for i in range(n):
        ans += (a[i] * b[n - 1 - i]) % mod
    return ans % mod

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(solve(n, a, b))
