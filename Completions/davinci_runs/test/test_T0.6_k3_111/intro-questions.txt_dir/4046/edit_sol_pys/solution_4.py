
# Solution

n = int(input())
q = list(map(int, input().split()))
p = [0] * n

for i in range(n - 1):
    p[i + 1] = p[i] + q[i]

if max(p) - min(p) != n - 1:
    print(-1)
else:
    print(*p)
