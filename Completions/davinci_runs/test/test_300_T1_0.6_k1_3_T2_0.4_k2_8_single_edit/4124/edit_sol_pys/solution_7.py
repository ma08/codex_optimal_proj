
def solve(s, t):
    if s == t:
        return 0
    else:
        if len(s) < len(t):
            return len(t) - len(s)
        else:
            return len(s) - len(t)


if __name__ == '__main__':
    s = input()
    t = input()
    print(solve(s, t))
