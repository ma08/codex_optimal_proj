
s = input()
t = input()

print("".join([s[i] for i in range(len(s)) if s[i] != t[i]]))
