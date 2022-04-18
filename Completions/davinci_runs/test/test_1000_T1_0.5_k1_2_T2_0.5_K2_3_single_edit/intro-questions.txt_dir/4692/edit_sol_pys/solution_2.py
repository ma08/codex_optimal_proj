def get_factors(n):
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    return factors


def is_perfect(n):
    factors = get_factors(n)
    sum = 0
    for f in factors:
        sum += f
    return sum == n

for i in range(1, 1000):
    if is_perfect(i):
        print(i)
