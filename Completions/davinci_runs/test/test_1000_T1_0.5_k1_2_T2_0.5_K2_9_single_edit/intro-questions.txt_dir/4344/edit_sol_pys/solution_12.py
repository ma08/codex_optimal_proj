
n, k = map(int, input().split())
A = list(map(int, input().split()))

if len(set(A)) < k:
    print('NO')
else:
    print('YES')
    for i in range(n):
        if k > 0:
            if A[i] not in A[:i]:
                print(i+1, end=' ')
                k -= 1
