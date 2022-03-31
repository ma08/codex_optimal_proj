
def solve():
    n = int(input())
    s = input()
    l = 0
    r = 0
    for i in range(n):
        if s[i] == '(':
            l += 1
        else:
            if l > 0:
                l -= 1
            else:
                r += 1
    print(2 * (l + r))

solve()
