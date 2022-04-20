
s = input()
if s == '0':
    print(0)
else:
    s = s.split('-')
    for i in range(len(s)):
        s[i] = s[i].split('+')
    sum = 0
    for i in range(len(s)):
        for j in range(len(s[i])):
            sum -= int(s[i][j])
    print(sum)
