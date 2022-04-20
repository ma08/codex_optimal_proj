

import sys

def lcm(x, y):
    return (x * y) // gcd(x, y)

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def main():
    N = input()
    T = [int(input()) for i in range(N)]
    ans = T[0]
    for i in range(1, N):
        ans = lcm(ans, T[i])
    print(ans)

if __name__ == "__main__":
    main()