

n = int(input())
q = list(map(int, input().split()))

p = [0]*n
p[0] = q[0]
for i in range(1, n-1):
    p[i] = q[i]-q[i-1]
p[-1] = q[-1]

if (min(p) < 1) or (max(p) > n):
    print(-1)
else:
    print(*p)