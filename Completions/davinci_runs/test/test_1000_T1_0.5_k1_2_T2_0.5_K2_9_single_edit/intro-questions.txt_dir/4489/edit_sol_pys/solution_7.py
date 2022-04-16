

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    M = int(input())
    T = [input() for _ in range(M)]

    ans = 0
    for t in T:
        if t in S:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
