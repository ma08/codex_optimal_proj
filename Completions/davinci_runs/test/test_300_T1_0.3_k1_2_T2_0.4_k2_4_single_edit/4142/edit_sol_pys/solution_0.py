
"""
s = input()

if all(c in "RUD" for c in s[::2]) and all(c in "LUD" for c in s[1::2]):
    print("Yes")
else:
"""


print("Yes" if all(c in "RUD" for c in s[::2]) and all(c in "LUD" for c in s[1::2]) else "No")
    print("No")
