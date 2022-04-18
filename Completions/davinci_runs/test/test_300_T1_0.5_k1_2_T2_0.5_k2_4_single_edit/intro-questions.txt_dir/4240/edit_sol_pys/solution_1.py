import sys

s = input()
t = input()

if s == t:
    print("Yes")
    sys.exit()

for i in range(len(s)):
    s = s[-1] + s[:-1]
    if s == t:
        print("Yes")
        sys.exit()

print("No")
