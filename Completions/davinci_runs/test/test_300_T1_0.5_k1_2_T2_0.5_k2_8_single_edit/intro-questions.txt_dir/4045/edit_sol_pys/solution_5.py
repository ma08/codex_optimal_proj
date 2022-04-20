

n = int(input())
s = input()
t = input()

if len(set(s+t)) == 2:
    if len(set(s)) == 1:
        print("NO")
    elif len(set(t)) == 1:
        print("NO")
    else:
        print("NO")
else:
    print("YES")
    print("a"*n+"b"*n+"c"*n)
