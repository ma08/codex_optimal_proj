import math

def is_prime(n):
    if n == 2:
        return True
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def get_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def solve(n):
    primes = get_primes(n)
    for p in primes:
        if n % p == 0:
            return p
    return n

def main():
    n = int(input())
    print(solve(n))

if __name__ == '__main__':
    main()



def main():
    n = int(input())
    primes = get_primes(n)
    for p in primes:
        if n % p == 0:
            print(p)
            return
    print(n)

if __name__ == '__main__':
    main()

def main():
    n = int(input())
    primes = get_primes(n)
    for p in primes:
        if n % p == 0:
            print(p)
            return
    print(n)

if __name__ == '__main__':
    main()

def main():
    n = int(input())
    primes = get_primes(n)
    for p in primes:
        if n % p == 0:
            print(p)
            return
    print(n)

if __name__ == '__main__':
    main()

def main():
    a1, b1, a2, b2 = list(map(int, input().split()))
    a3, b3, a4, b4 = list(map(int, input().split()))
    gunnar = (b1 - a1 + 1) * (b2 - a2 + 1)
    emma = (b3 - a3 + 1) * (b4 - a4 + 1)
    if gunnar > emma:
        print('Gunnar')
    elif gunnar < emma:
        print('Emma')
    else:
        print('Tie')

if __name__ == '__main__':
    main()
