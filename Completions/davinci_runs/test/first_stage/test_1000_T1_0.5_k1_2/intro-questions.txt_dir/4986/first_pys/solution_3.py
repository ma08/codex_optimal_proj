

s = input()
t = input()

sticky = []

for i in range(len(s)):
    if s[i] != t[i]:
        sticky.append(s[i])

print("".join(sticky))