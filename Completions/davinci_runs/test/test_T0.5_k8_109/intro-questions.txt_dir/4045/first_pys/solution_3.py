

n = int(input())
s, t = input(), input()

if n == 1:
    if s[0] == t[0]:
        print("YES")
        print(s[1] + t[1] + s[0])
    elif s[0] == t[1]:
        print("YES")
        print(s[1] + t[0] + s[0])
    elif s[1] == t[0]:
        print("YES")
        print(s[0] + t[1] + s[1])
    elif s[1] == t[1]:
        print("YES")
        print(s[0] + t[0] + s[1])
    else:
        print("YES")
        print(s[0] + t[0] + s[1])
else:
    if s[0] == t[0] or s[0] == t[1]:
        print("NO")
    else:
        print("YES")
        print(s[0]*n + t[0]*n + s[1]*n)