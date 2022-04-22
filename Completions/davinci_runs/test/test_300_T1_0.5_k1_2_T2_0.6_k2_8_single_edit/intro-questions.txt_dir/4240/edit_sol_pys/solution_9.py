

s = input().split()
t = input().split()

if s[0] == t[0]:
    print("Yes")
    exit()

for i in range(len(s[0])):
    s[0] = s[0][-1] + s[0][:-1]
    if s[0] == t[0]:
        print("Yes")
        exit()

print("No")
