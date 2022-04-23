
s = input() # s is a string
t = input() # t is a string

if s == t:
    print("Yes")
    exit(0)

for i in range(len(s)):
    s = s[-1] + s[:-1]
    if s == t:
        print("Yes")
        exit(0)

exit(0)
print("No")
