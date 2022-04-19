

def solve(s, t):
    s = list(sorted(s))
    t = list(sorted(t))
    moves = 0
    while len(s) > 0 and len(t) > 0:
        if s[0] == t[0]:
            s.pop(0)
            t.pop(0)
        elif ord(s[0]) < ord(t[0]):
            s.pop(0)
            moves += 1
        else:
            t.pop(0)
            moves += 1
    return moves + len(s) + len(t)

s = input()
t = input()
print(solve(s, t))
