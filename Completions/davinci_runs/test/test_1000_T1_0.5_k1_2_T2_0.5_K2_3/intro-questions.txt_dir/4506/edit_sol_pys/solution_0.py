
def solve(n, a, b):
    a.sort(reverse=True)
    b.sort(reverse=True)
    ans = 0
    for i in range(n):
        ans += (a[i] * b[i]) % 998244353
    return ans

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(solve(n, a, b))
