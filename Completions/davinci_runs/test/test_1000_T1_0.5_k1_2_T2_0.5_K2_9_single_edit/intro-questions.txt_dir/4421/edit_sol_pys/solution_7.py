import sys

input = sys.stdin.readline


n, k = map(int, input().split())
d = list(map(int, input().split()))
d.sort(reverse=True)

def possible(a, b):
    return (a + b) % k == 0

ans = 0
l, r = 0, n - 1
while l < r:
    if possible(d[l], d[r]):
        ans += 2
        l += 1
        r -= 1
    else:
        ans += 1
        r -= 1

if l == r:
    ans += 1

print(ans)
