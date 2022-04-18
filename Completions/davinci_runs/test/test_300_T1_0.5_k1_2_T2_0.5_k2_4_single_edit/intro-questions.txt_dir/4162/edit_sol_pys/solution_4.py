
from math import gcd

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ret = k
    for i in range(n):
        ret = min(ret, a[i] // gcd(a[i], k))
    print(ret * k)

if __name__ == '__main__':
    main()
