s = input()

if s[0] == s[1] or s[2] == s[3]:
    print('YES')
elif s[0] == s[2] or s[1] == s[3]:
    print('YES')
elif s[0] == s[3] or s[1] == s[2]:
    print('YES')
else:
    print('NO')
