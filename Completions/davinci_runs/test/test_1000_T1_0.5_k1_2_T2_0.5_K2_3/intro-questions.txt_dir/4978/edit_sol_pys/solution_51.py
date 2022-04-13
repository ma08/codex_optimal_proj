import sys
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, m=DVSR): return pow(x, m - 2, m)
def DIV(x, y, m=DVSR): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1] * i % DVSR)
    return res


def main():
    N = II()
    arr = LI()

    res = [0] * N
    for i in range(N-1, -1, -1):
        res[i] = res[i+1] + arr[i]
    print(res)


if __name__ == "__main__":
    main()
