
s, t = input(), input()  # input two strings

if s == t:
    print("Yes")
    exit()

for i in range(len(s)):
    s = s[-1] + s[:-1]  # rotate the string
    if s == t:
        print("Yes")
        exit()

print("No")
