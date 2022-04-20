

n = int(input())
q = list(map(int, input().split()))

if sum(q) != 0:
    print(-1)
    exit()

p = []
for i in range(1, n+1):
    p.append(i)

for i in range(1, n):
    if q[i-1] < 0:
        p[i-1], p[i+q[i-1]] = p[i+q[i-1]], p[i-1]
    else:
        p[i+q[i-1]], p[i] = p[i], p[i+q[i-1]]

print(*p)