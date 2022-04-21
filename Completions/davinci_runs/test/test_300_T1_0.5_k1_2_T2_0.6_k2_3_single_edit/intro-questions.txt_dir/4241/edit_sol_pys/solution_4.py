
def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    P = list(map(int, input().split()))
    A.sort()
    P.sort()
    # Pの値の順番にAの値を並べる
    ans = 0
    for i in range(N):
        ans += A[i] * P[N-i-1]
    print(ans)
solve()
