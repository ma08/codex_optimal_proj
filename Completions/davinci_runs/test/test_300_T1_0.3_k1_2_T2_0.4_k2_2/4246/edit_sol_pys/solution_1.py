

s = input()
t = input()

correct = 0
for i in range(3):
    if s[i] == t[i]:  # if文の条件式
        correct += 1

print(correct)
