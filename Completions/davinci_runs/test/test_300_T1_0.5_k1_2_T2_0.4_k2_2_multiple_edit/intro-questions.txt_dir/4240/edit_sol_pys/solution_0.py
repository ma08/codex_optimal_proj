

s = input()  # input string
t = input()  # input string

if s == t:  # if strings are equal
    print("Yes")
else:  # if strings are not equal
    if len(s) == len(t):  # if strings have the same length
        for i in range(len(s)):  # cycle for
            if s == t:  # if strings are equal
                print("Yes")
                break
            else:
                s = s[-1] + s[:-1]
        else:
            print("No")
    else:
        print("No")
