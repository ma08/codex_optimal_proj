
s = input().split('-')
sum = 0
for i in range(len(s)):
    if '+' in s[i]:
        s[i] = s[i].split('+')
        for j in range(len(s[i])):
            sum += int(s[i][j])
    else:
        sum -= int(s[i])
print(sum)
