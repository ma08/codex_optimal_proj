n = int(input())
for i in range(n):
    s = input().split('-')
    for i in range(len(s)):
        s[i] = s[i].split('+')
    sum = 0
    for i in range(len(s)):
        for j in range(len(s[i])):
            sum -= int(s[i][j])
    print(sum)
