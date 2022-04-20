


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return a * b // gcd(a, b)


def solution():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [0]
    for i in range(1, n):
        b.append(lcm(a[i - 1], a[i]))
    min_lcm = min(b)
    for i in range(1, n):
        if b[i] == min_lcm:
            print(i, i + 1)
            return


solution()