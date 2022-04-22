
s = input()

if(s[0] == s[1] or s[1] == s[2] or s[2] == s[3]):  # Same number cannot be next to each other
    print("Bad")
else:
    print("Good")
