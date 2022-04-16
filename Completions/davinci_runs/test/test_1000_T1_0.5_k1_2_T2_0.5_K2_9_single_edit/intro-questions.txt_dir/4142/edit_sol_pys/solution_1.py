

s = input()

if (len(s) % 2 == 0) and (s[0] in ['R', 'U', 'D']) and (s[-1] in ['R', 'U', 'D']):
    print('Yes')
else:
    print('No')
