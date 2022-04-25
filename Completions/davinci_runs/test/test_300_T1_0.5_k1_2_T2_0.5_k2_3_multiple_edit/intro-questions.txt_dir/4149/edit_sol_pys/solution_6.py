

def convert_to_prime_numbers(n):
    primes = []
    i = 2
    while len(primes) < n + 1:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_numbers():
    primes = []
    i = 2
    while True:
        if is_prime(i):
            primes.append(i)
        i += 1
        yield primes

def solve(n, b):
    primes = convert_to_prime_numbers(n + 1)
    a = []
    for i in range(n):
        if i % 2 == 1:
            a.append(b[i])
        else:
            if b[i] in primes:
                a.append(primes.index(b[i]) + 1)
            else:
                a.append(b[i])
    return a

def main():
    n = int(input())
    b = [int(i) for i in input().split(' ')]
    a = solve(n, b)
    print(' '.join([str(i) for i in a]))

if __name__ == '__main__':
    main()
