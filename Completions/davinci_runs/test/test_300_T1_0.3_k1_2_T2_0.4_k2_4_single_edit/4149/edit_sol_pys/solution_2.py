
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_prime(n):
    i = 3
    while n > 1:
        if is_prime(i):
            n -= 1
        i += 1
    return i


def find_divisor(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n


def solve(n, b):
    a = []
    for i in range(n):
        if b[2*i] == b[2*i + 1]:
            a.append(find_prime(b[2*i]))
        else:
            a.append(b[2*i] * b[2*i + 1] // find_divisor(b[2*i] * b[2*i + 1]))
    return a

n = int(input())
b = list(map(int, input().split()))
a = solve(n, b)
print(*a)
