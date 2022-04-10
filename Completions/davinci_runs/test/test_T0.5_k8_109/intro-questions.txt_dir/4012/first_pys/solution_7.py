

def solve(a, b, c):
    if b % a == 0 and c % b == 0:
        return (0, a, b, c)
    if b % a == 0:
        return (1, a, b, c - (c % b))
    if c % b == 0:
        return (1, a - (a % b), b, c)
    if b % a == 0:
        return (1, a - (a % b), b, c)
    return (2, a - (a % b), b - (b % a), c)

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    res, a, b, c = solve(a, b, c)
    print(res)
    print(a, b, c)