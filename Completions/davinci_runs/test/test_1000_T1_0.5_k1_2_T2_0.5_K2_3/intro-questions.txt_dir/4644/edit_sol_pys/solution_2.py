
t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if sum(a) % 2 == 0:
        print("NO")
    else:
        print("YES")


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primeFactors(n):
    prime_factors = []
    for i in range(2, n):
        if n % i == 0 and isPrime(i):
            prime_factors.append(i)
    return prime_factors


def main():
    n = int(input())
    primes = primeFactors(n)
    print(primes)


if __name__ == "__main__":
    main()
