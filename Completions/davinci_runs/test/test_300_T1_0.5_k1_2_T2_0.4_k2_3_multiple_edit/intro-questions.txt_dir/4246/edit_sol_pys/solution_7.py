

s = input()  # input the string
t = input()  # input the string
correct = 0
for i in range(len(s)):
    if s[i] == t[i]:
        correct += 1

print(correct)
