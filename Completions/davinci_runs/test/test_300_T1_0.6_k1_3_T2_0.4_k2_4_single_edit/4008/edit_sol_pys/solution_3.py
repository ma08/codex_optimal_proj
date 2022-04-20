
n, k = map(int, input().split())
a = list(map(int, input().split()))[:n]
if len(set(a)) >= k:
    print('YES')
    for i in range(n): print(i % k + 1, end=' ')
else: print('NO')
