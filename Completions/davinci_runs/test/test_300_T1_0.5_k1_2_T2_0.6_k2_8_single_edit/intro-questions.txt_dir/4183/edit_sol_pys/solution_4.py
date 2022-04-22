

def main():
    N, K = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    ans = 1
    for i in range(N):
        if A[i] <= K:
            ans = lcm(ans, A[i])
    print(ans)

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    N = int(input())
    T = [int(input()) for _ in range(N)]
    ans = 1
    for t in T:
        ans = lcm(ans, t)
    print(ans)

if __name__ == '__main__':
    main()
