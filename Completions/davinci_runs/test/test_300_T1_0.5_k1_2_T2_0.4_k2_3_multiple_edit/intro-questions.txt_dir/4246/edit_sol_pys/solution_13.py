

s = input()  # input the string 1
t = input()  # input the string 2

correct = 0

for i in range(len(s)):
    if s[i] == t[i]:
        correct += 1

print(correct)
