

n = int(input())
q = [int(i) for i in input().split()]

if len(q) != n-1:
    print(-1)

p = [0]*n
p[0] = q[0]

for i in range(1,n-1):
    p[i] = p[i-1] + q[i]

p[n-1] = p[n-2] + q[n-2]

if min(p) < 1 or max(p) > n:
    print(-1)
    exit()

for i in range(n):
    if p.count(p[i]) > 1:
        print(-1)
        exit()

print(*p)