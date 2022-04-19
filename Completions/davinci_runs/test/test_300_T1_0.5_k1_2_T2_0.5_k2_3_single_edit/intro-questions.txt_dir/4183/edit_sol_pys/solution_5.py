N = int(input())
T = [int(input()) for _ in range(N)]


def lcm(x, y):
    return (x * y) // gcd(x, y)

print(reduce(lcm, T))
