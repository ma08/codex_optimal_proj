import math


def solve(n, m, a, l, r, primes):
    for i in range(m):
        print(primes[r[i]]-primes[l[i]-1])

def get_primes(n, primes):
    for i in range(2, n):
        prime = True
        for j in range(i):
            if primes[j] > math.sqrt(i):
                break
            if i % primes[j] == 0:
                prime = False
                break
        if prime:
            primes.append(i)

if __name__ == '__main__':
    n, m = [int(i) for i in raw_input().split()]
    a = [int(i) for i in raw_input().split()]
    l = []
    r = []
    for i in range(m):
        l.append(int(raw_input().split()[0]))
        r.append(int(raw_input().split()[1]))
    primes = [2]
    get_primes(max(a), primes)
    solve(n, m, a, l, r, primes)
