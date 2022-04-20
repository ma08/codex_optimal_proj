import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def lcm(a, b):
    return a * b // gcd(a, b)
def main():
    n = int(input())
    t = [int(input()) for _ in range(n)]
    ans = t[0]
    for i in range(1, n):
        ans = lcm(ans, t[i])
    print(ans)
if __name__ == '__main__':
    main()
