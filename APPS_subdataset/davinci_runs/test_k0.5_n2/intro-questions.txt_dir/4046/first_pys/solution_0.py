

# SOLUTION
# Note: This is a very nice problem.
# 1. We can see that the sum of the array q is equal to the sum of the array p.
# 2. For each i, we can see that p[i] = q[i] + p[i-1].
# 3. We can see that for each i, p[i] >= 1 and p[i] <= n.

from sys import stdin, stdout

n = int(stdin.readline())
q = [int(x) for x in stdin.readline().split()]

p = [0]*n

if sum(q) != n*(n+1)//2:
    stdout.write("-1")
    exit()

for i in range(1, n):
    p[i] = q[i-1] + p[i-1]
    if p[i] < 1 or p[i] > n:
        stdout.write("-1")
        exit()

stdout.write(" ".join([str(x) for x in p]))