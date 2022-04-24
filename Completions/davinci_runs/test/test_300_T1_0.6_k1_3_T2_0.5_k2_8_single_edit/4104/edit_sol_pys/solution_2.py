s = input()
if s[0] == '-':
    s = input().split('-')
    for i in range(len(s)):
        s[i] = s[i].split('+')
    sum = 0
    for i in range(len(s)):
        for j in range(len(s[i])):
            sum -= int(s[i][j])
    print(sum)
else:
    s = input().split('+')
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    print(sum)
