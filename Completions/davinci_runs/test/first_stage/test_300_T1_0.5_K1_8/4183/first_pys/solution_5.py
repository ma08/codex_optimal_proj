

N = int(input())
T = [int(input()) for i in range(N)]

def gcd(m, n):
    if m % n == 0:
        return n
    return gcd(n, m % n)

def lcm(m, n):
    return m * n // gcd(m, n)

def lcm_list(l):
    if len(l) == 1:
        return l[0]
    return lcm(l[0], lcm_list(l[1:]))

print(lcm_list(T))