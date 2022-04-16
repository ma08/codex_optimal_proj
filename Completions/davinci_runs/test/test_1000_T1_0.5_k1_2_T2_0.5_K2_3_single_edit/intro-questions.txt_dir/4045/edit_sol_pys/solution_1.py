
n = int(input())
s = input()
t = input()

if len(set(s)) == 2:
    if s[0] == s[-1]:
        print("YES")
        print("abc"*n)
    else:
        print("NO")
else:
    print("YES")
    print("abc"*n)
