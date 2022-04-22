

n = int(input())
s = input()
t = input()

if len(set(s+t)) == 3:
    print("YES")
    print("abc" * n)
elif len(set(s+t)) == 2:
    if s[0] == s[1]:
        print("YES")
        print("abc" * n)
    elif t[0] == t[1]:
        print("YES")
        print("abc" * n)
    else:
        print("NO")
else:
    print("YES")
    print("abc" * n)
