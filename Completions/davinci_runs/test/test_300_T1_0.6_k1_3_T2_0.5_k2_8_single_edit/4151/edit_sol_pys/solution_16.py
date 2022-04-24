

from sys import stdin, stdout

def read_ints():
    return [int(x) for x in stdin.readline().strip().split()][0]

def read_int():
    return [int(x) for x in stdin.readline().strip().split()]

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
    pass

if __name__ == "__main__":
    main()
