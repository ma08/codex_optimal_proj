

def main():
    N = int(input())
    S = [int(input()) for _ in range(N)]
    M = int(input())
    T = [int(input()) for _ in range(M)]

    ans = 0
    for s in S:
        if s in T:
            ans -= 1
        else:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
