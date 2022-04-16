

def solve(n, a, b, k):
    a.sort()
    b.sort()
    ans = 0
    for i in range(n):
        ans += (a[i] * b[n - 1 - i]) % k
    return ans % k

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(solve(n, a, b))
