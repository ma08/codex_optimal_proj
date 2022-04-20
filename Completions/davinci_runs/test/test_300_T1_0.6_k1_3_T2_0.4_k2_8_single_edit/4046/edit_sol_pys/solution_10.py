
n = int(input())
q = [int(x) for x in input().split()]

if not all([-n < x < n for x in q]):
    print(-1)
else:
    p = [1]
    for i in range(n - 1):
        p.append(p[i] + q[i])
    if not all([1 <= x <= n for x in p]):
        print(-1)
    else:
        print(' '.join([str(x) for x in p]))
