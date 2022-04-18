
s = input()
t = input()

sticky = []
for i in range(len(s)): sticky.append(s[i]) if s[i] != t[i] else 0

print("".join(set(sticky)))
