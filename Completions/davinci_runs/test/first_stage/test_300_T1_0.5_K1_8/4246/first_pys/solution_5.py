

s = input()
t = input()

correct_days = 0

for i in range(3):
    if s[i] == t[i]:
        correct_days += 1

print(correct_days)