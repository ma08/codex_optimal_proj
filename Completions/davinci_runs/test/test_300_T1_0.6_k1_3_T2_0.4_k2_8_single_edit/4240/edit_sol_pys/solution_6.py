
s = input()
t = input()

if s == t:
    print("Yes")
else:
    for _ in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            print("Yes")
            exit()
    print("No")
