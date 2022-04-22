

n = int(input())
s = input()
t = input()

if len(set(s+t)) == 3 and s[0] != s[1] and t[0] != t[1]:
    print("YES")
    print("a"*n+"b"*n+"c"*n)
elif len(set(s+t)) == 2 and s[0] == s[1] and t[0] == t[1]:
    print("YES")
    print("a"*n+"b"*n+"c"*n)
else:
    print("NO")
    print("a"*n+"b"*n+"c"*n)
