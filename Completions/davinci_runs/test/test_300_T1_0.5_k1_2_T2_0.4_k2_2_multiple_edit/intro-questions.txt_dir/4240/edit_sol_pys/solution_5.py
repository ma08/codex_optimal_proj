

s = input()  # input string 1
t = input()  # input string 2

if s == t:  # if string 1 is equal to string 2
    print("Yes")
else:
    if len(s) == len(t):  # if length of strings 1 and 2 are equal
        for i in range(len(s)):
            if s == t:  # if string 1 is equal to string 2
                print("Yes")
                break
            else:
                s = s[-1] + s[:-1]  # rotate string 1
        else:
            print("No")
    else:
        print("No")
