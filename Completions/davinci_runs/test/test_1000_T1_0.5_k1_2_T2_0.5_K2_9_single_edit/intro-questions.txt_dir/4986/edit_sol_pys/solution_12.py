
s = input()
t = input()

sticky = set()
for i in range(len(s)):
    if s[i] != t[i]:
        sticky.add(s[i])

print("".join(sticky))
