
s = input()
t = input()

if s == t:
    print("Yes")
    exit(0)

for i in range(len(s)):
    s = s[-1] + s[:-1]
    if s == t:
        print("Yes")
        exit(0)

print("No")
