
s = input()
t = input()

for i in range(0, len(s)):
    if s[i] != t[2 * i]:
        print(s[i], end="")
