
s = input().split('-')
for i in range(len(s)):
    s[i] = s[i].split('+')
Sum = 0
for i in range(len(s)):
    for j in range(len(s[i])):
        Sum -= int(s[i][j])
print(Sum)
