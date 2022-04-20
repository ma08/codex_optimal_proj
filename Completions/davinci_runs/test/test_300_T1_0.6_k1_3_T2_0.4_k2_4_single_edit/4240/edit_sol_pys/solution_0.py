

s = input()  # type: str
t = input()  # type: str

if s == t:
    print("Yes")
else:
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            print("Yes")
            exit()
    print("No")
