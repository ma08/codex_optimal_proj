import math


def divisor(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors


n = int(input())

divisors = divisor(n)

if len(divisors) % 2 == 0:
    print(divisors[len(divisors) // 2 - 1])
else:
    print(divisors[len(divisors) // 2])
