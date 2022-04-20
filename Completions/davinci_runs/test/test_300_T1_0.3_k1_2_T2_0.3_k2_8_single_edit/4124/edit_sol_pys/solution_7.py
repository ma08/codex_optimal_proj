
def solve(s, t):
    return sum(s[i] != t[i] for i in range(len(s)))

s = input()
t = input()
print(solve(s, t))
