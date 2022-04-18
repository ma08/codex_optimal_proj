

s = input("s: ")
t = input("t: ")

sticky = []

for i in range(min(len(s), len(t))):
    if s[i] != t[i]:
        sticky.append(s[i])

print("".join(sticky))
