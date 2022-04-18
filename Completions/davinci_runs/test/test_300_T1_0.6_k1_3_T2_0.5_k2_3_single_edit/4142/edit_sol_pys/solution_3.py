

s = input("")

if len(s) % 2 == 0:
    if s[0] == "R" or s[0] == "U" or s[0] == "D":
        for i in range(1, len(s), 2):
            if s[i] != "L" and s[i] != "U" and s[i] != "D":
                print("No" + "\n")
                break
        else:
            print("Yes" + "\n")
    else:
        print("No" + "\n")
else:
    if s[0] == "L" or s[0] == "U" or s[0] == "D":
        for i in range(1, len(s), 2):
            if s[i] != "R" and s[i] != "U" and s[i] != "D":
                print("No" + "\n")
                break
        else:
            print("Yes" + "\n")
    else:
        print("No" + "\n")
