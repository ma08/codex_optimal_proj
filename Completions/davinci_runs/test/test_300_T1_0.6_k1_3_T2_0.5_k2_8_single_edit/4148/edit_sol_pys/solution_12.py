
n = int(input())
s = input()

for i in range(len(s)):
    if ord(s[i]) >= 65 and ord(s[i]) <= 90:
        s = s[:i] + chr(ord(s[i]) + n) + s[i + 1:]
    elif ord(s[i]) >= 97 and ord(s[i]) <= 122:
        s = s[:i] + chr(ord(s[i]) + n) + s[i + 1:]

print(s)
