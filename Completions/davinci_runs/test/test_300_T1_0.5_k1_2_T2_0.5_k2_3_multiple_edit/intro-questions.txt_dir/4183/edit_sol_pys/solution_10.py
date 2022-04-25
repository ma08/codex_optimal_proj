
def gcd(m, n):
    while n:
        m, n = n, m % n
    return m

def lcm(m, n):
    return m * n // gcd(m, n)

def main():
    N = int(input())
    T = [int(input()) for _ in range(N)]
    ans = 1
    for t in T:
        ans = lcm(ans, t)
    print(ans)

if __name__ == '__main__':
    main()
