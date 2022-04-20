
n = int(input())
q = list(map(int, input().split()))

q.sort()

p = [0]*n
p[0] = q[0]

for i in range(1, n):
    p[i] = q[i] + p[i-1]

print(*p)
