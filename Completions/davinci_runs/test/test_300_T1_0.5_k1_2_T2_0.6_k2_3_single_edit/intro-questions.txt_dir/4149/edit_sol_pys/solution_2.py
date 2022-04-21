

def get_primes(n):
    if n < 2:
        return []
    primes = [2]
    for i in range(3, n + 1, 2):
        is_prime = True
        for j in range(3, int(i**0.5) + 1, 2):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

def solve(b):
    primes = get_primes(max(b))
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
    a = solve(b)
    print(' '.join([str(i) for i in a]))

if __name__ == '__main__':
    main()
