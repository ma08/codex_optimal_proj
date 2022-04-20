

n, k = map(int, input().split())

if n < k or n > k * 2:
    print('NO')
else:
    print('YES')
    if n % k == 0:
        print(*(n // k for _ in range(k)))
    else:
        print(*(n // k for _ in range(k - 1)), n - n // k * (k - 1))