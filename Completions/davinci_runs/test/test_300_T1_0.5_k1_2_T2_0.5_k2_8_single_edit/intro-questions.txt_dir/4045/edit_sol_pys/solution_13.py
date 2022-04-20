
n = int(input())
s = input()
t = input()

if len(set(s+t)) == 3:  # 3文字なら
    print("YES")
    print("a"*n+"b"*n+"c"*n)
elif len(set(s+t)) == 2:  # 2文字なら
    if s[0] == s[1]:  # sが2文字なら
        print("YES")
        print("a"*n+"b"*n+"c"*n)
    elif t[0] == t[1]:
        print("YES")
        print("a"*n+"b"*n+"c"*n)
    else:
        print("NO")
else:
    print("YES")
    print("a"*n+"b"*n+"c"*n)
