import sys
from functools import reduce



def gcd(*numbers):
    return reduce(lambda a, b: gcd(a, b), numbers)

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
