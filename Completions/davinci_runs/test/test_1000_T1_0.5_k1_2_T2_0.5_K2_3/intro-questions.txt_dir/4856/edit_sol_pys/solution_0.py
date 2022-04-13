
a = []
s = input()

for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        a.append(i - 1)
        a.append(i)
        print(a)
        a = []
