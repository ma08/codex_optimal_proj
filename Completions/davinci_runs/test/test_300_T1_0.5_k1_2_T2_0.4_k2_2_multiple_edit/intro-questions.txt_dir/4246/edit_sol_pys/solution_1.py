

s = input("Enter string s: ")
t = input("Enter string t: ")
 
correct = 0

for i in range(len(s)):
    if s[i] == t[i]:
        correct += 1

print(correct)
