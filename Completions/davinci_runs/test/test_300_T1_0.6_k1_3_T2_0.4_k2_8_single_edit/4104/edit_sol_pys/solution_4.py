s = input().split('-')  # input string
for i in range(len(s)):  # split by '-'
    s[i] = s[i].split('+')  # split by '+'
sum = 0
for i in range(len(s)):
    for j in range(len(s[i])):
        sum -= int(s[i][j])
print(sum)
