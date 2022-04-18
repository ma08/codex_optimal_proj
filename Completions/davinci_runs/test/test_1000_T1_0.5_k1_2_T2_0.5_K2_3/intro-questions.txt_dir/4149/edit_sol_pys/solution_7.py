

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(n):
    primes = []
    i = 2
    while i <= n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

def convert_to_primes(n):
    primes = get_primes(n)
    d = {}
    for i, val in enumerate(primes):
        d[val] = i + 1
    return d

def solve(n, b):
    primes = convert_to_primes(n)
    a = []
    for i, val in enumerate(b):
        if i % 2 == 0:
            a.append(val)
        else:
            if val in primes.keys():
                a.append(primes[val])
            else:
                a.append(val)
    return a

def main():
    n = int(input())
    b = [int(i) for i in input().split()]
    a = solve(n, b)
    print(' '.join([str(i) for i in a]))

if __name__ == '__main__':
    main()
