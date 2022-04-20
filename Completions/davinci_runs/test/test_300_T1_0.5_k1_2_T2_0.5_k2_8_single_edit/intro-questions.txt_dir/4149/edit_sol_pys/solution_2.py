

def convert_to_primes(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        primes = []
        i = 2
        while len(primes) < n:
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

def get_primes():
    primes = []
    i = 2
    while True:
        if is_prime(i):
            primes.append(i)
        i += 1
        yield i

def solve(n, b):
    primes = convert_to_primes(n)
    a = []
    for i, val in enumerate(b):
        if i % 2 == 0:
            a.append(val)
        else:
            if val in primes:
                a.append(primes.index(val) + 1)
            else:
                a.append(val)
    return a

def main():
    n = int(input())
    b = [int(i) for i in input().split(' ')]
    a = solve(n, b)
    print(' '.join([str(i) for i in a]))

if __name__ == '__main__':
    main()
