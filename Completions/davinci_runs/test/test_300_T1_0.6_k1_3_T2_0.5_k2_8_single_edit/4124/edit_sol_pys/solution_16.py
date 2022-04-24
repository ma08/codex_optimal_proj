

def solve(s, t):
    return len(s) - len(t) if len(s) > len(t) else len(t) - len(s)

if __name__ == '__main__':
    s = input()
    t = input()
    print(solve(s, t))
