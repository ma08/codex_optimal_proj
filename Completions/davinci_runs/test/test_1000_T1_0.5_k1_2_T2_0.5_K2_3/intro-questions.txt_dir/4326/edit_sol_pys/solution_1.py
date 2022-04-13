

# 素因数分解
# 素数
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())

if n % 3 == 0:
    print(n // 3 * 2)
elif n % 3 == 1:
    print((n - 4) // 3 * 2 + 1)
else:


    print((n - 2) // 3 * 2 + 1)
