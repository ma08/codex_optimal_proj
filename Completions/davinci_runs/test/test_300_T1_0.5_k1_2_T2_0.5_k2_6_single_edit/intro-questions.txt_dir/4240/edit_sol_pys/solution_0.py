

s = input().strip()
t = input().strip()

if len(s) != len(t):
    print("No")
else:
    if s == t:
        print("Yes")
        exit()
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            print("Yes")
            exit()
    print("No")
