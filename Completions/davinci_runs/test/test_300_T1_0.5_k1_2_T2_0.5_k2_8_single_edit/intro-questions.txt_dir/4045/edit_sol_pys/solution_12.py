

n = int(input())
s = input()
t = input()

if len(set(s+t)) == 3 and n == 1:
    print("YES")
    print(s[0]+t[0]+t[1])
elif len(set(s+t)) == 2:
    if s[0] == s[1]:
        print("YES")
        print(s[0]+t[0]+t[1])
    elif t[0] == t[1]:
        print("YES")
        print(s[0]+t[0]+t[1])
    else:
        print("NO")
else:
    print("YES")
    print(s[0]+t[0]+t[1])
