
s = input().split('-')
sum = 0
for i in range(len(s)):
    if '+' in s[i]:
        s[i] = s[i].split('+')
        sum -= int(s[i][0])
        sum += int(s[i][1])
    else:
        sum -= int(s[i])
print(sum)
