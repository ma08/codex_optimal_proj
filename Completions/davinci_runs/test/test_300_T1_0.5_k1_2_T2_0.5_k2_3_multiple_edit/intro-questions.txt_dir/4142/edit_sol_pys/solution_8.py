
s = input()

if len(s) % 2 == 0:
    if s[0] in 'RUD' and s[-1] in 'RUD':
        print('Yes')
    else:
        print('No')
else:
    print('Yes')
