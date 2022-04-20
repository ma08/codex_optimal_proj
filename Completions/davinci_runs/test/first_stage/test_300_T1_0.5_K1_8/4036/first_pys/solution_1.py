

def solve(n, k):
    if n < k:
        return 'NO'
    if n == k:
        return 'YES\n' + ' '.join(str(1) for _ in range(k))
    if n > k * 2:
        return 'NO'
    if n == k + 1:
        return 'YES\n' + ' '.join(str(2) for _ in range(k - 1)) + ' 1'

    n -= k
    a = []
    while n > 0:
        if n >= 2:
            a.append(2)
            n -= 2
        else:
            a.append(1)
            n -= 1
    return 'YES\n' + ' '.join(str(i) for i in a) + ' ' + ' '.join(str(2) for _ in range(k - len(a)))

n, k = map(int, input().split())
print(solve(n, k))