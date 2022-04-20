# coding: utf-8

s = input()
t = input()

if s == t:
    print("Yes")
else:
    if len(s) == len(t):
        for i in range(len(s)):
            if s == t:
                print("Yes")
                break
            else:
                s = s[-1] + s[:-1]
        else:
            print("No")
    else:
        print("No")
