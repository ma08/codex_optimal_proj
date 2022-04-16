
n = int(input())
s = input()
t = input()

if len(set(s + t)) == 3:
    print("YES")
    print("a" * n + "b" * n + "c" * n)
elif len(set(s + t)) == 2:
    if s[0] == s[1]:
        print("YES")
        print("a" * n + "b" * n + "c" * n)
    elif t[0] == t[1]:
        print("YES")
        print("a" * n + "b" * n + "c" * n)
    else:
        print("NO")
else:
    print("YES")
    print("a" * n + "b" * n + "c" * n)
