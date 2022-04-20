
import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += gcd(a[i], a[j])
    print(ans)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    main()
