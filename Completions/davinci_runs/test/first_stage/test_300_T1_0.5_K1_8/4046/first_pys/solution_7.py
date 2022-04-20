

n = int(input())
q = [int(x) for x in input().split()]

p = [0]*n
p[0] = 0

for i in range(1, n):
    p[i] = p[i-1] + q[i-1]

if any(x < 1 or x > n for x in p):
    print("-1")
    exit()

if len(set(p)) != n:
    print("-1")
    exit()

print(" ".join(map(str, p)))