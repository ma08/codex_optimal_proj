

s = input("")
t = input("")

if s == t:
    print("Yes", end="")
else:
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            print("Yes", end="")
            exit()
    print("No", end="")
