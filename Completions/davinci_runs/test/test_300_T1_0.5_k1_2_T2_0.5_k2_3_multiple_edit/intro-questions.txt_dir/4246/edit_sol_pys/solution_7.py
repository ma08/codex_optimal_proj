s = input()
t = input()

correct_count = 0

for i in range(len(s)):
    if s[i] == t[i]:
        correct_count += 1

print(correct_count)
