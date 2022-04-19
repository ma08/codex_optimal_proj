
n = int(input())
q = list(map(int, input().split()))

if sum(q) != 0 or max(q) > n or min(q) < 1:
    print(-1)
    exit()

p = [0] * n
p[0] = q[0]
for i in range(1, n-1):
    p[i] = q[i-1] + q[i]
p[n-1] = q[n-2]

print(*p)
