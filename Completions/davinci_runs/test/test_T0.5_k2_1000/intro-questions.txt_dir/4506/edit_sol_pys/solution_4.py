
def solve(n, A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    ans = 0
    for i in range(n):
        ans += (A[i] * B[i]) % 998244353
    return ans

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solve(n, A, B))
