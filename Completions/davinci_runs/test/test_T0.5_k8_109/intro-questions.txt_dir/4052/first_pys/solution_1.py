

n = int(input())
s = input()
t = input()

def check(s, t):
    if s == t:
        return True
    else:
        return False

def move(s, t, c):
    if c == n:
        return check(s, t)
    else:
        return move(s, t, c+1) or move(s[:c] + s[c+1] + s[c] + s[c+2:], t, c+1) or move(s[:c] + s[c+2] + s[c+1] + s[c] + s[c+3:], t, c+1)

if move(s, t, 0):
    print(0)
else:
    print(-1)