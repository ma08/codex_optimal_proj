
import sys

def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def solve(n):
    ans = 1
    for i in range(n):
        ans = lcm(ans, int(sys.stdin.readline()))
    return ans

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(solve(n))
