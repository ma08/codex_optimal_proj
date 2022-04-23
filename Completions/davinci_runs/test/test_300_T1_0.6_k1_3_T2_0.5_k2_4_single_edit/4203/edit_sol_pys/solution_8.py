

# -----Answer-----
s = input()  # read a line with a single integer
# 'hello'
# s = int(input())
# '1234'
# s = list(map(int, input().split()))
# '1 2 3 4'
# A = [int(s) for s in input().split()]
# '1 2 3 4'

if s[0] == 'A' and s[1].islower() and s[2].islower() and s[3] == 'C' and s[4:].islower():
    print("AC")
else:
    print("WA")

# -----Answer-----
# s = input()
#
# if s[0] == 'A' and s[1].islower() and s[2].islower() and s[3] == 'C' and s[4:].islower():
#     print("AC")
# else:
#     print("WA")
