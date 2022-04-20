
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
            print("No")
    else:
        print("No")
