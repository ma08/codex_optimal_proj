import sys
import math
import random


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def get_prime(n):
    if n < 2:
        return 2
    if n % 2 == 0:
        n += 1
    while not is_prime(n):
        n += 2
    return n

def get_random(a, b):
    return random.randint(a, b)

def get_random_prime(a, b):
    return get_prime(get_random(a, b))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

def gen_keys():
    p = get_random_prime(100, 200)
    q = get_random_prime(300, 400)
    n = p * q
    f = (p - 1) * (q - 1)
    d = get_random(1, f)
    while gcd(f, d) != 1:
        d = get_random(1, f)
    e = d
    while gcd(f, e) != 1:
        e += 1
    return (e, n), (d, n)

def encrypt(s, key):
    e, n = key
    c = []
    for i in s:
        c.append(ord(i) ** e % n)
    return c

def decrypt(c, key):
    d, n = key
    s = []
    for i in c:
        s.append(chr(i ** d % n))
    return ''.join(s)

def main():
    s = input('Enter string to encrypt: ')
    public_key, private_key = gen_keys()
    print('Public key: ', public_key)
    print('Private key: ', private_key)
    c = encrypt(s, public_key)
    print('Encrypted string: ', c)
    s = decrypt(c, private_key)
    print('Decrypted string: ', s)

if __name__ == '__main__':
    main()
