

s = input()

if s[1] == s[2] or s[2] == s[3] or s[3] == s[4]:
    print("Bad")
else:


s = input()
s = s.replace("eraser", "")
s = s.replace("erase", "")
s = s.replace("dreamer", "")
s = s.replace("dream", "")

if s:
    print("NO")
else:
    print("YES")
    print("Good")
