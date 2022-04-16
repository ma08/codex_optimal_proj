

s = input()
t = input()

sticky = []

for i in range(len(s)):
    if s[i] == t[i]:
        pass
    else:
        sticky.append(s[i])

print("".join(sticky))
