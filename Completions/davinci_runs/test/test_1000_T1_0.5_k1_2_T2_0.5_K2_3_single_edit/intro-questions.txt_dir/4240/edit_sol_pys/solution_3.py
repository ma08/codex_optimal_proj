

s = input()
t = input()

if s == t:
    print("Yes")
else:
    for i in range(len(s)):
        if s == t:
            print("Yes")
            break
        else:
            s = s[-1] + s[:-1]
    else:
        print("No")
