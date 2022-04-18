

s = input("Enter a string:")

for i in range(1, len(s), 2):
    s = s[:i] + "x" + s[i:]
print(s)
