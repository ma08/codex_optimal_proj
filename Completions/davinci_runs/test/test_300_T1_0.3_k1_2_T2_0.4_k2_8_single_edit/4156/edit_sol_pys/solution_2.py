

# Solution for https://open.kattis.com/problems/bijele

pieces_needed = [1, 1, 2, 2, 2, 8]
pieces_owned = [int(x) for x in input().split()]

x = [0] * (n + 1)

for i in range(1, n + 1):
    x[i] = x[i - 1] + a[i - 1]

x.sort()

ans = 0

for i in range(1, n + 1):
    if x[i] - x[i - 1] > 0:
        ans += x[i] - x[i - 1]

print(min(ans, w + 1))
