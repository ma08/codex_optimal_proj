def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


n = int(input())
a = list(map(int, input().split()))[:n]

for i in a:
    if is_prime(i):
        print('YES')
    else:
        print('NO')
