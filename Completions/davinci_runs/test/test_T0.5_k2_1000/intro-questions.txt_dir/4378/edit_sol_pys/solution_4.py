
n = int(input())
s = input()

t = ""

if s[0] == s[1]:
    t += "R" if s[0] == "G" else "G"
else:
    t += s[0]

if s[n - 1] == s[n - 2]:
    t += "R" if s[n - 1] == "G" else "G"
else:
    t += s[n - 1]

for i in range(1, n - 1):
    if s[i] == s[i - 1] and s[i] == s[i + 1]:
        t += "R" if s[i] != "R" else "G"
    elif s[i] == s[i - 1] or s[i] == s[i + 1]:
        t += "R" if s[i] != "R" else "G"
    else:
        t += "R" if s[i] != "R" else "G"

num_changes = sum(1 for i in range(n) if t[i] != s[i])

print(num_changes)

print(t)
