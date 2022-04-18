
n, k = map(int, input().split())
a = list(map(int, input().split()))

if len(set(a)) < k or k == 0:
    print('NO')
else:
    print('YES')
    for i in range(n):
        if k > 0:
            if a[i] not in a[:i] and k > 0:
                print(i+1, end=' ')
                k -= 1
