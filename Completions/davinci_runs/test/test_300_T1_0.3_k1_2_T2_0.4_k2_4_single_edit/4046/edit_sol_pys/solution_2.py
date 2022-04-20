

n = int(input())
q = list(map(int, input().split()))

if sum(q) != 0 or n == 1:
    print(-1)
    exit()

p = [0] * n
p[0] = q[0] + q[1]
for i in range(1, n):
    p[i] = q[i-1]

if min(p) < 1 or max(p) > n:
    print(-1)
    exit()

print(*p)
