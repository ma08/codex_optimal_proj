
s = input("input s: ")
t = input("input t: ")
correct = 0

for i in range(len(s)):
    if s[i] == t[i]:
        correct += 1

print(correct)
