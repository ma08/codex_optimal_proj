

n = int(input())
q = [int(i) for i in input().split()]

p = [0] * n

if sum(q) != 0:
    print(-1)
    exit()

for i in range(n-1):
    if p[i] + q[i] < 1 or p[i] + q[i] > n:
        print(-1)
        exit()
    p[i + 1] = p[i] + q[i]

if p[0] == 0:
    for i in range(n):
        p[i] = i + 1
else:
    for i in range(n):
        p[i] = i + 1 - p[i]

for i in range(n):
    print(p[i], end=" ")