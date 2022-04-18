

n = int(input())  # input n
s = input().split()

if len(s) != n:  # check length of string
    print("Something is fishy")
else:
    for i in range(n):
        if s[i] == "mumble":  # if mumble, skip
            continue
        if int(s[i]) != i+1:  # check if int(s[i]) is equal to i+1
            print("Something is fishy")
            break
    else:
        print("Makes sense")
