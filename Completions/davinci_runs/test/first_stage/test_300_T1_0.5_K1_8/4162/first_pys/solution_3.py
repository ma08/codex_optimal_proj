

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    lcm = a[0]
    for i in range(1, n):
        lcm = lcm * a[i] // gcd(lcm, a[i])
    ans = 0
    for i in range(n):
        ans += lcm * modinv(lcm // a[i], a[i]) % lcm
    print(ans % lcm)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def modinv(a, mod):
    b = mod
    u = 1
    v = 0
    while b:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u %= mod
    if u < 0:
        u += mod
    return u

if __name__ == '__main__':
    main()