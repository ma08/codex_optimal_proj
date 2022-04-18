

def solve(n, s, t):
    ans = [0] * n
    for i in range(n):
        ans[i] = s[i] + t[i]
    return ''.join(map(str, ans))

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(solve(n, a, b))
