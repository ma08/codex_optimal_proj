
def solve(n, a, b):
    if n == 1:
        return 1
    if n == 2:
        return 3
    return solve(n - 1, a, b) * a + solve(n - 2, a, b) * b
a, b, n = map(int, input().split())
print(solve(n, a, b))
