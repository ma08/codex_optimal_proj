import sys

n = int(input())
q = list(map(int, input().split()))
if sum(q) != 0:
    print("-1")
    sys.exit(0)
i = 0
p = [0] * (n + 1)
for j in range(1, n + 1):
    p[j] = p[j - 1] + q[j - 1]
    if p[j] < 1 or p[j] > n:
        print("-1")
        sys.exit(0)

p = p[1:]
print(*p)
