

def main():
    N = int(input())
    A, B, C, D, E = list(map(int, input().split()))

    ans = 0

    for n in range(N):
        d = n // (C + D)
        e = d // (A + B)
        ans = max(ans, n + d + e)

    print(ans)

if __name__ == "__main__":
    main()
