
s = input().split('-')
for i in range(len(s)):
    s[i] = s[i].split('+')
sum = 0
for i in range(len(s)):
    for j in range(len(s[i])):
        sum += int(s[i][j])
    if i > 0:
        sum -= int(s[i][j])
print(sum)
