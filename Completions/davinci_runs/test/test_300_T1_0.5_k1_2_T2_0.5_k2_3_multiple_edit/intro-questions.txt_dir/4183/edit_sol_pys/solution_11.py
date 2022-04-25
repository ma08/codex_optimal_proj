

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y / gcd(x, y)

def main():
    N = int(input())
    T = [int(input()) for _ in range(N)]
    ans = 1.0
    for t in T:
        ans = lcm(ans, t)
    print(ans)

if __name__ == '__main__':
    main()
