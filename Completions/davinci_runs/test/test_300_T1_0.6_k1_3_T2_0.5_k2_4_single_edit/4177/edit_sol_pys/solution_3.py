
s = input("Enter your name: ")

for i in range(len(s)):
    s = s[:i] + "x" + s[i+1:]
print(s)
