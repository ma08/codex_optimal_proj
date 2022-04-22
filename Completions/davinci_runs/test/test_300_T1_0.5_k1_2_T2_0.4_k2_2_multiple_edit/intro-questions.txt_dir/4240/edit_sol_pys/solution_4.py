

s = input() #input string
t = input() #input string

if s == t: #if strings are equal
    print("Yes")
else: #if strings are not equal
    if len(s) == len(t): #if strings have the same length
        for i in range(len(s)): #cycle for
            if s == t: #if strings are equal
                print("Yes")
                break
            else: #if strings are not equal
                s = s[-1] + s[:-1]
        else: #if strings are not equal
            print("No")
    else: #if strings have not the same length
        print("No")
