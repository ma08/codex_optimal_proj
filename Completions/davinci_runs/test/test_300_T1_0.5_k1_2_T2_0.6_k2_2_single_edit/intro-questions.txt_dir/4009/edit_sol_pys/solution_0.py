

a, b, c = map(int, input().split())
s = list(input())

if s[c-1] == '0':
    s[c-1] = '1'
else:
    s[c-1] = '0'
    for i in range(c, b):
        if s[i] == '0':
            s[i] = '1'
            break
        else:
            s[i] = '0'

print(n.count('0'))
