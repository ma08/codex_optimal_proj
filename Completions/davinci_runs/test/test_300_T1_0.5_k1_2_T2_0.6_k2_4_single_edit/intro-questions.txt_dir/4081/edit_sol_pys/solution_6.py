

# SOLUTION 1

def solution():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    if N == K:
        print(max(A) - min(A))
        return

    ans = A[N - 1] - A[0]
    for i in range(N - K + 1):
        ans = min(ans, A[i + K - 1] - A[i])
    print(ans)


problem_C2()
