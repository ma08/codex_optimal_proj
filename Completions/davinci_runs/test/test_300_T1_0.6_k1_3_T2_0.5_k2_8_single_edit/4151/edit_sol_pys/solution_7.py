

from sys import stdin, stdout

def read_ints():
    return [int(x) for x in input().strip().split()]

def read_int():
    return int(input().strip())

MOD = 998244353
MAXN = 200000

fac = [1]
inv_fac = [1]

for i in range(1, MAXN+1):
    fac.append(fac[-1] * i % MOD)
    inv_fac.append(inv_fac[-1] * pow(i, MOD-2, MOD) % MOD)

def binom(n, k):
    return fac[n] * inv_fac[k] * inv_fac[n-k] % MOD

def mod_inv(x):
    return pow(x, MOD-2, MOD)

def main():
    n = read_int()
    a = read_ints()
    count = [0] * (n+1)
    for x in a:
        count[x] += 1
    for i in range(1, n+1):
        if count[i] > 0:
            k = count[i]
            count[i] = binom(k, k-1)
    for i in range(1, n+1):
        if count[i] > 0:
            for j in range(i*2, n+1, i):
                count[j] = (count[j] - count[i]) % MOD
    result = 1
    for i in range(1, n+1):
        if count[i] > 0:
            result = result * count[i] % MOD
    print(result)

if __name__ == "__main__":
    main()
