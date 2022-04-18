# This is the first line

s = input("Enter s: ")
t = input("Enter t: ")

correct = 0

for i in range(len(s)):
    if s[i] == t[i]:
        correct += 1

print(correct)
