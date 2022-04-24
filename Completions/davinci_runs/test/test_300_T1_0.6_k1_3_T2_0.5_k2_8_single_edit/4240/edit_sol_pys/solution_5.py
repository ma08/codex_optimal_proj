

s = input().rstrip()
t = input().rstrip()

if s == t:
    print("Yes")
else:
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            print("Yes")
            exit()
    print("No")
