
s = input()
t = input()

for i in range(len(s)-1):
    s = s[1:] + s[0]
    if s == t:
        print("Yes")
        exit()

print("No")
