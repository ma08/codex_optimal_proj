
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

    smallest_num = a[0]  # 初期値
    for i in range(1, n):
        smallest_num = lcm(smallest_num, a[i])

    print(len(find_factors(smallest_num)))

main()
