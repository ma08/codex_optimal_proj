import math

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans = max(ans, gcd(a[i], a[j]))
    print(ans)

if __name__ == '__main__':
    main()
