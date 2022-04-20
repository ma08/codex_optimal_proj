

# -----Answer-----
s = input().split()

if s[0][0] == 'A' and s[0][1].islower() and s[0][2].islower() and s[0][3] == 'C' and s[0][4:].islower():
    print("AC")
else:
    print("WA")

# -----Answer-----
# s = input().split()
#
# if s[0][0] == 'A' and s[0][1].islower() and s[0][2].islower() and s[0][3] == 'C' and s[0][4:].islower():
#     print("AC")
# else:
#     print("WA")
