

def solve(a, b, c):
    days = 7
    return min(days, 1 + a + min(b, c))

a, b, c = map(int, input().split())
print(solve(a, b, c))