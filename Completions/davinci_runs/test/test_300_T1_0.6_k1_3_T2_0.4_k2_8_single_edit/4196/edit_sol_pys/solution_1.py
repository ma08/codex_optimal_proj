import math


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    gcd = a[0]
    for i in range(1, n):
        gcd = math.gcd(gcd, a[i])
    print(gcd)
