

n = int(input())
s = input()
t = input()

if len(set(s+t)) == 3: # 3文字使う
    print("YES")
    print("a"*n+"b"*n+"c"*n)
elif len(set(s+t)) == 2: # 2文字使う
    if s[0] == s[1]: # sが同じ
        print("YES")
        print("a"*n+"b"*n+"c"*n)
    elif t[0] == t[1]: # tが同じ
        print("YES")
        print("a"*n+"b"*n+"c"*n)
    else:
        print("NO")
else: # 1文字使う
    print("YES")
    print("a"*n+"b"*n+"c"*n)
