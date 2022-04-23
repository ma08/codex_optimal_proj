from math import sqrt

N, M = map(int, input().split())


def get_divisors(n):
    divisors = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    return divisors


divisors = get_divisors(M)

divisors.sort()

for i in range(len(divisors)):
    if divisors[i] >= N:
        print(divisors[i])
        exit()

print(1)
