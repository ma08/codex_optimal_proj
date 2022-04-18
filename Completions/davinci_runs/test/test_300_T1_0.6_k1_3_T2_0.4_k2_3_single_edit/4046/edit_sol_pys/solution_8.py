
n = int(input())
q = list(map(int, input().split()))

q.sort()

p = [0]*n
p[0] = q[0]

for i in range(1, n):
    p[i] = q[i] + p[i-1]

p[n-1] = q[n-2] + p[n-2]

if p[n-1] < 1:
    print(-1)
else:
    print(*p)
