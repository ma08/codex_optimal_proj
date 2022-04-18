
s = input()
t = input()

correct = 0 #number of correct characters

for i in range(len(s)):
    if s[i] == t[i]: #if the characters are the same
        correct += 1

print(correct)
