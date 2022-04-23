
s = input().split('-')
for i in range(len(s)):
    s[i] = s[i].split('+')
sum1 = 0
for i in range(len(s)):
    for j in range(len(s[i])):
        sum1 -= int(s[i][j])
print(sum1)
