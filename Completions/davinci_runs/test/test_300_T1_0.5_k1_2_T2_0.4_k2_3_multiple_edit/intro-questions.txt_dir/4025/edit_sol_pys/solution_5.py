# https://codeforces.com/contest/1341/problem/A

def solve(n, a, b, c, d):
    if a-b > n*d or b-a > n*c:
        return False
    return True

t = int(input())

for _ in range(t):
    n, a, b, c, d = [int(x) for x in input().split()]
    print("Yes" if solve(n, a, b, c, d) else "No")
