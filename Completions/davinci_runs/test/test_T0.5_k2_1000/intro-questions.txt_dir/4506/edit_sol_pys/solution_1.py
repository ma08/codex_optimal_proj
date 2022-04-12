
def solve(n, A, B):
    A.sort()
    B.sort()
    ans = 0
    for i in range(n):
        ans += (A[i] * B[n - 1 - i])
    return ans

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solve(n, A, B))
