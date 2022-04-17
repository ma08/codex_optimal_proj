

s = input()
t = input()

if s == t:
    print("Yes")
    exit()

for i in range(1, len(s)):
    s = s[-i:] + s[:-i]
    if s == t:
        print("Yes")
        exit()

print("No")
