

s = input() # s is the string inputted by the user
t = input() # t is the string inputted by the user

if s == t: # if the strings are the same
    print("Yes")
elif len(s) == len(t): # if the strings are the same length
    for i in range(len(s)):
        if s == t: # if the strings are the same
            print("Yes")
            break
        else:
            print("No")
    else:
        print("No")
