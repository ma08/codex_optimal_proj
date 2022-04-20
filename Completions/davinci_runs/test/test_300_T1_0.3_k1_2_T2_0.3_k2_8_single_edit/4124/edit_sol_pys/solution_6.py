
def solve(s, t):
    moves = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            moves += 1
    return moves

s = input()
t = input()
print(solve(s, t))
