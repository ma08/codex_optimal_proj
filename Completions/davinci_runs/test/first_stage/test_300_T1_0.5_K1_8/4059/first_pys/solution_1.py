

import math

N = int(input())

def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True

def factorize(n):
    """
    nを素因数分解する
    """
    a = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                a.append(i)
                n //= i
                break
    return a

def count_divisor(n):
    """
    nの約数の個数を数える
    """
    a = factorize(n)
    m = {}
    for num in a:
        if num in m:
            m[num] += 1
        else:
            m[num] = 1
    divisor = 1
    for num in m.values():
        divisor *= (num + 1)
    return divisor

def main():
    ans = 0
    for i in range(1, N + 1):
        if N % i == 0:
            ans += count_divisor(i)
    print(ans)

if __name__ == "__main__":
    main()