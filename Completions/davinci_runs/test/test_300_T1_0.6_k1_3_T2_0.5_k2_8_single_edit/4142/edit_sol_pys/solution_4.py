
ans = "Yes"
s = input()

if len(s) % 2 == 0:
    if s[0] == "R" or s[0] == "U" or s[0] == "D":
        for i in range(1, len(s), 2):
            if s[i] != "L" and s[i] != "U" and s[i] != "D":
                ans = "No"
                break;
    elif s[0] == "L" or s[0] == "U" or s[0] == "D":
        for i in range(1, len(s), 2):
            if s[i] != "R" and s[i] != "U" and s[i] != "D":
                ans = "No"
                break;
    else: ans = "No"
else:
    ans = "No"

print(ans)
