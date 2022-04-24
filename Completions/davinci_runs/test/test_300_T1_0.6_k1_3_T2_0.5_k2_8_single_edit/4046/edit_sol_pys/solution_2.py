

n = int(input())
q = [int(x) for x in input().split()]
p = [1]
for i in range(1, n):
    p.append(p[-1] + q[i-1])
if not all([1 <= x <= n for x in p]):
    print(-1)
else:    
    if not all([-n < x < n for x in q]):
        print(-1)
    else:
        print(' '.join([str(x) for x in p]))
