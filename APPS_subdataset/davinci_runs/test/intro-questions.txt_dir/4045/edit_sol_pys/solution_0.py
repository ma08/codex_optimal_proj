
n = int(input())
s = input()
t = input()

def check(s, t):
    for i in range(2):
        if s[i] == t[0] and s[(i + 1) % 2] == t[1]:
            return True
    return False

if check(s, t):
    print("YES")
    print("a" * n + "b" * n + "c" * n)
elif check(t, s):
    print("YES")
    print("b" * n + "c" * n + "a" * n)
else:
    print("NO")
