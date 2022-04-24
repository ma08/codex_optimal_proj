

def get_primes():
    primes = [2]
    yield primes
    i = 3
    while True:
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
            yield primes
        i += 2

def get_prime_index(primes, n):
    return primes.index(n) + 1

def solve(n, b):
    primes = get_primes()
    a = [0] * n
    for i in range(n):
        if i % 2 == 1:
            next(primes)
        primes_list = next(primes)
        if b[i] in primes_list:
            a[i] = get_prime_index(primes_list, b[i])
        else:
            a[i] = b[i]
    return a

def main():
    n = int(input())
    b = [int(i) for i in input().split(' ')]
    a = solve(n, b)
    print(' '.join([str(i) for i in a]))

if __name__ == '__main__':
    main()
