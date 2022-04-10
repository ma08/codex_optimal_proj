


def solve(n, s, t):
    if n == 1:
        return "YES\n" + "abc"[s.index("a")] * 3
    if n == 2:
        return "YES\n" + "abc"[s.index("a")] * 2 + "abc"[t.index("a")] * 2
    if n == 3:
        return "YES\n" + "abc"[s.index("a")] + "abc"[t.index("a")] + "abc"[s.index("a")] * 2 + "abc"[t.index("a")] * 2
    if n == 4:
        return "YES\n" + "abc"[s.index("a")] * 3 + "abc"[t.index("a")] * 3
    if n == 5:
        return "YES\n" + "abc"[s.index("a")] * 2 + "abc"[t.index("a")] * 2 + "abc"[s.index("a")] * 2 + "abc"[t.index("a")] * 2
    if n == 6:
        return "YES\n" + "abc"[s.index("a")] + "abc"[t.index("a")] + "abc"[s.index("a")] * 3 + "abc"[t.index("a")] * 3
    if n == 7:
        return "YES\n" + "abc"[s.index("a")] * 2 + "abc"[t.index("a")] * 2 + "abc"[s.index("a")] * 3 + "abc"[t.index("a")] * 3
    if n == 8:
        return "YES\n" + "abc"[s.index("a")] * 3 + "abc"[t.index("a")] * 3 + "abc"[s.index("a")] * 3 + "abc"[t.index("a")] * 3
    if n == 9:
        return "YES\n" + "abc"[s.index("a")] * 2 + "abc"[t.index("a")] * 2 + "abc"[s.index("a")] * 4 + "abc"[t.index("a")] * 4
    return "YES\n" + "abc"[s.index("a")] * 3 + "abc"[t.index("a")] * 3 + "abc"[s.index("a")] * 4 + "abc"[t.index("a")] * 4


if __name__ == "__main__":
    n = int(input())
    s = input()
    t = input()
    print(solve(n, s, t))