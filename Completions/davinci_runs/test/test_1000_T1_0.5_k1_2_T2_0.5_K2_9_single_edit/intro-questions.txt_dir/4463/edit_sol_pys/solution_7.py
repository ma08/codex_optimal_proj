

s = input()
t = input()

if len(s) < len(t):
    print("Yes")
elif len(s) > len(t):
    print("No")
else:
    for i in range(len(s)):
        if s[i] < t[i]:
            print("Yes")
            break
        elif s[i] > t[i]:
            print("No")
            break
        else:
            if i == len(s) - 1:

                print("No")
