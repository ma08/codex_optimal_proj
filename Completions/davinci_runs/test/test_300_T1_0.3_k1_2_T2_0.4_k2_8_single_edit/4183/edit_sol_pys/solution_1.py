
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    N = int(input())
    t = [int(input()) for _ in range(N)]
    ans = t[0]
    for i in range(1, N):
        ans = lcm(ans, t[i])
    print(ans)

if __name__ == '__main__':
    main()
