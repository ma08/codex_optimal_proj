n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print('YES')
else:
    m = max(a)
    if sum(a) == m*n:
        print('YES')
    else:
        print('NO')
