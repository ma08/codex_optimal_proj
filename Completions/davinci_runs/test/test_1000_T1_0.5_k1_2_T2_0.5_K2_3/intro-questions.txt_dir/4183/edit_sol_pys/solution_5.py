import math

def gcd(x, y):
    return math.gcd(x, y)

def lcm(x, y):
    return x * y // math.gcd(x, y)

def main():
    N = int(input())
    T = [int(input()) for _ in range(N)]
    ans = 0
    for t in T:
        ans = lcm(ans, t)
    print(ans)

if __name__ == '__main__':
    main()
