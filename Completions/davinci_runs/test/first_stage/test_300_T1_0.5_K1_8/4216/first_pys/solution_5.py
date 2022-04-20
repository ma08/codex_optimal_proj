

N = int(input())

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: return False
    return True

def digit_count(n):
    c = 0
    while n > 0:
        c += 1
        n //= 10
    return c

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def main():
    if is_prime(N):
        print(digit_count(N))
    else:
        a = prime_factorize(N)
        b = []
        for n in a:
            b.append(digit_count(n))
        print(max(b))

if __name__ == '__main__':
    main()