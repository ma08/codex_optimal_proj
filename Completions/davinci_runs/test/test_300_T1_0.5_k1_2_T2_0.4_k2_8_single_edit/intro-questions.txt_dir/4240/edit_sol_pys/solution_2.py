
s = input()
t = input()

if s == t:
    print("Yes")
else:
    if len(s) != len(t):
        print("No")
    else:
        for i in range(len(t)):
            s = s[-1] + s[:-1]
            if s == t:
                print("Yes") 
                exit()
        else:
            print("No")
    else:
        print("No")
