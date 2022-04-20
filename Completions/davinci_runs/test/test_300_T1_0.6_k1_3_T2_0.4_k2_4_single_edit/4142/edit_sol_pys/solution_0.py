
s = "RUDLUDR"
s = input()

if len(s) % 2 == 0:
    if s[0] == "R" or s[0] == "U" or s[0] == "D":
        for i in range(1, len(s), 2):
            if s[i] != "L" and s[i] != "U" and s[i] != "D" or s[i+1] != "R" and s[i+1] != "U" and s[i+1] != "D":
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")
else:
    if s[0] == "L" or s[0] == "U" or s[0] == "D":
        for i in range(1, len(s), 2):
            if s[i] != "R" and s[i] != "U" and s[i] != "D" or s[i+1] != "L" and s[i+1] != "U" and s[i+1] != "D":
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")
