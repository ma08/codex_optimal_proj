

def main():
    N, M = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    """
    P[i][j] = time for stage j, worker i
    T[i][j] = time for stage j, worker i
    """
    T = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if j == 0:
                T[i][j] = P[i][j]
            else:
                T[i][j] = T[i][j-1] + P[i][j]
    T.sort()
    ans = []
    for i in range(N):
        ans.append(T[i][-1])
    print(*ans)


if __name__ == "__main__":
    main()
