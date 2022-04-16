
n, k = map(int, input().split())

def solve(n, k, ans=0):
    if k == 0:
        return ans
    elif k == 1:
        return ans + (n + 1) / 2
    else:
        return solve(n, k - 1, ans + (n + 1) / 2)

print(solve(n, k))
