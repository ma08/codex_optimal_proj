

def solve(s, t):
    if s == t:
        return 0
    else:
        return max(len(s), len(t)) - min(len(s), len(t))

if __name__ == '__main__':
    s = input()
    t = input()
    print(solve(s, t))
