
n = int(input())
q = [int(x) for x in input().split()]

if not all([-n < x < n for x in q]):
    print(-1)
else:
    p = [1] * n
    for i in range(1, n): p[i] = p[i-1] + q[i-1]
    if all([1 <= x <= n for x in p]): print(' '.join([str(x) for x in p]))
    else: print(-1)
