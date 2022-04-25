

s = input("input s: ").strip()
t = input("input t: ").strip()

correct = 0

for i in range(len(s)):
    if s[i] == t[i]:
        correct += 1

print(correct)
