
n = int(input())
q = list(map(int, input().split()))

if sum(q) != 0:
    print(-1)
    exit()

p = [0] * n
p[0] = q[0]
for i in range(1, n - 1):
    p[i] = q[i - 1] + q[i]
p[n - 1] = q[n - 2]

if min(p) < 1 or max(p) > n:
    print(-1)
    exit()

print(*p)
