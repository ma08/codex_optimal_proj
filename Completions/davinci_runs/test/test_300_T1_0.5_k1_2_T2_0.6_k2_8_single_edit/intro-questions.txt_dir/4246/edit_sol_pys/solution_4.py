

s = input()
t = input()

correct = 0

for i in range(len(s)):		# if s[i] == t[i] then increment correct
    if s[i] == t[i]:
        correct += 1

print(correct)
