

s = input()

if s[0] == s[1] and s[2] == s[3]:
    print('Yes')
elif s[0] == s[2] and s[1] == s[3]:
    print('Yes')
elif s[0] == s[3] and s[1] == s[2]:
elif s[0] == s[1] and s[0] == s[2] and s[0] == s[3]:
    print('Yes')
    print('Yes')
else:
    print('No')
