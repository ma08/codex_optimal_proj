
def solve(s, t):
    return len(s) + len(t) - 2 * len(set(s) & set(t))

s = input()
t = input()
print(solve(s, t))
