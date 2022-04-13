
import math

def solve():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    sum_A = [0] * (N + 1)
    sum_B = [0] * (M + 1)
    for i in range(N):
        sum_A[i + 1] = sum_A[i] + A[i]

    for i in range(M):
        sum_B[i + 1] = sum_B[i] + B[i]

    j = M
    ans = 0
    for i in range(N + 1):
        if sum_A[i] > K:
            break
        while sum_A[i] + sum_B[j] > K:
            j -= 1
        ans = max(ans, i + j)

    print(ans)

if __name__ == "__main__":
    solve()
