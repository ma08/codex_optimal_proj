

def solve(n, k, a):
    ans = (k - 1) * (n - 1) + 1
    return ans

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(solve(n, a, b))
