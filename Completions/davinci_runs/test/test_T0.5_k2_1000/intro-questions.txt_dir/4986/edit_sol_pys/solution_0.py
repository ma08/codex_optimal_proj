s = input()
t = input()

sticky = ""

for i in range(len(s)):
    if s[i] != t[i]:
        sticky += s[i]

print(sticky)
