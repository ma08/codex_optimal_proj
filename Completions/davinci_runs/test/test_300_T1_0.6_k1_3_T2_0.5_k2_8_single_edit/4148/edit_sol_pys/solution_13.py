
n = int(input())
s = input()

if n <= len(s):
    for i in range(len(s)):
        s = s[:i] + chr(ord(s[i]) + n) + s[i + 1:]

print(s)
