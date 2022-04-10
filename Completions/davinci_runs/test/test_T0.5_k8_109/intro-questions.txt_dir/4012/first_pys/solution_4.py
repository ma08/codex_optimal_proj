

def solve(a, b, c):
    res = 0
    if b % a != 0:
        res += (b % a)
        b += (b % a)
    if c % b != 0:
        res += (c % b)
        c += (c % b)
    return res, a, b, c

t = int(input())
for i in range(t):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    res, a, b, c = solve(a, b, c)
    print(res)
    print(a, b, c)