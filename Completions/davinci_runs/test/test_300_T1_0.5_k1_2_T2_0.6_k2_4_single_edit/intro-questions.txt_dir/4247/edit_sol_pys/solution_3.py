

s = list(input())
t = list(input())

for i in range(len(s)):
    if s[i] == t[i]:
        s[i] = 'a'
        t[i] = 'a'
if s == t:
    print('Yes')
else:
    print('No')
