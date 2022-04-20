

def main():
    N, M, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = float('inf')
    for i in range(1 << N):
        cost = 0
        skill = [0] * M
        for j in range(N):
            if ((i >> j) & 1):
                cost += A[j][0]
                for k in range(M):
                    skill[k] += A[j][k + 1]
        if all(s >= X for s in skill):
            ans = min(ans, cost)
    print(-1 if ans == float('inf') else ans)

if __name__ == '__main__':
    main()
