

s = input() # s is the string inputted by the user
t = input() # t is the string inputted by the user

if s == t: # if the strings are the same
    print("Yes")
else:
    if len(s) == len(t): # if the strings are the same length, rotate the string
        for i in range(len(s)):
            if s == t: # if the strings are the same, print yes and break the loop
                print("Yes")
                break
            s = s[-1] + s[:-1] # rotate the string
        else: # if the strings are not the same, print no
            print("No")
    else:
        print("No")
