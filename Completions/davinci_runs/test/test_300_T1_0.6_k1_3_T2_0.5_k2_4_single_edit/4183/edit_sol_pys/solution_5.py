
import sys

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def solve(n):
    ans = 1
    for _ in range(n):
        ans = lcm(ans, int(input()))
    return ans

if __name__ == '__main__':
    n = int(input())
    print(solve(n))
