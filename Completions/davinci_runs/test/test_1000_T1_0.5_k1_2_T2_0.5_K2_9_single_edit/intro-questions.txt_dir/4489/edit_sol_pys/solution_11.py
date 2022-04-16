

def main():
    N = int(input())
    S = [int(input()) for _ in range(N)]
    M = int(input())
    T = [int(input()) for _ in range(M)]

    ans = 0
    for t in T:
        ans += S.count(t)

    print(ans)

if __name__ == '__main__':
    main()
