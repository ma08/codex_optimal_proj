

n = int(input())
q = [int(x) for x in input().split()]

p = [0] * n
p[0] = q[0] + 1

for i in range(1, n):
    p[i] = p[i-1] + q[i]

if any([x <= 0 or x > n for x in p]):
    print(-1)
else:
    print(' '.join([str(x) for x in p]))