

N, K = map(int, input().split())


def solve(N, K):
    if N % K == 0:
        return 0
    else:
        return 1


print(solve(N, K))
