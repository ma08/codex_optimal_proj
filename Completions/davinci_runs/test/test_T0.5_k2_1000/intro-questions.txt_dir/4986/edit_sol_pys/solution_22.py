
s = input("Enter the first string: ")
t = input("Enter the second string: ")

result = ''

for i in range(len(s)):
    if s[i] != t[i]:
        result += s[i]

print(result)
