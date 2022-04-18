def solve():
    N = int(input())
    W = list(map(int, input().split()))


    S1 = 0
    S2 = sum(W)

    ans = abs(S1 - S2)
    for i in range(1, N):
        S1 += W[i-1]
        S2 -= W[i-1]
        ans = min(ans, abs(S1 - S2))

    print(ans)

if __name__ == "__main__":
    solve()
