# https://codeforces.com/contest/1263/problem/A

def solve(a, b, c):
    if a < b:
        a, b = b, a
    if a < c:
        a, c = c, a
    if b < c:
        b, c = c, b
    if a == b == c:
        return 0
    if a == b:
        return c
    if a == c:
        return b
    if b == c:
        return a
    if a - b == 1 and b - c == 1:
        return 0
    if a - b == 1:
        return 1
    if b - c == 1:
        return 1
    if a - b > 1 and b - c > 1:
        return 2


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        print(solve(a, b, c))
