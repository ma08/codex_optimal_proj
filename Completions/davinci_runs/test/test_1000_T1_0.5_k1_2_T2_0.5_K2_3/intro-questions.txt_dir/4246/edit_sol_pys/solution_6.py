# This is the first line

s = input("")
t = input("")

correct = 0

for i in range(len(s)):
    if s[i] == t[i]:
        correct += 1

print(correct)
