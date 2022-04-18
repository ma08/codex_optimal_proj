

s = input()
t = input()

if s == t:
    print("Yes")
else:
    if len(s) == len(t):
        for _ in range(len(s)):
            if s == t:
                print("Yes")
                break
            else:
                s = s[-1] + s[:-1]
        else:
            print("No")
    else:
        print("No")
