
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def main():
    n = int(input())
    a = list(map(int, input().split()))

    smallest_number = a[0]
    for i in range(1, n):
        smallest_number = lcm(smallest_number, a[i])

    print(len(find_factors(smallest_number)))

main()
