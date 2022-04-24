
s = input().split('+')
s = s[::-1]
sum = 0
for i in range(len(s)):
    for j in range(len(s[i])):
        sum += int(s[i][j])
print(sum)
