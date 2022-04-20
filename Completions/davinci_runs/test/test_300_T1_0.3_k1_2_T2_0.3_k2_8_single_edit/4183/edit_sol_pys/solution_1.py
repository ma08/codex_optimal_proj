import sys
sys.setrecursionlimit(10**6)


def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A.sort()
    ans = 0
    for i in range(N-1):
        ans += A[i]
    ans += A[N-1] // 2
    print(ans)

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    N = int(input())
    T = [int(input()) for _ in range(N)]
    ans = T[0]
    for i in range(1, N):
        ans = lcm(ans, T[i])
    print(ans)

if __name__ == '__main__':
    main()
