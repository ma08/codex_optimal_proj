

s = input()
if s[0].isupper() and s[2] == "C" and s[1:].islower():
    print("AC")
else:
    print("WA")