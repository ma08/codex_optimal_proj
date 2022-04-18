
s = input()

if (len(s) % 2 == 0) and (s[0] in 'UD') and (s[-1] in 'UD'):
    print('Yes')
else:
    print('No')
