

s = input()
t = input()

correct = 0
for i in range(3):
    if s[i] == t[i]:
        correct += 1

print(correct)