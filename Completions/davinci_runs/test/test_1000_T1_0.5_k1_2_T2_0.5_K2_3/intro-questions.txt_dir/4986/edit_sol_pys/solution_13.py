
s = input("")
t = input("")

sticky = list(s)

for i in range(len(s)):
    if s[i] != t[i]:
        sticky[i] = t[i]

print("".join(sticky))
