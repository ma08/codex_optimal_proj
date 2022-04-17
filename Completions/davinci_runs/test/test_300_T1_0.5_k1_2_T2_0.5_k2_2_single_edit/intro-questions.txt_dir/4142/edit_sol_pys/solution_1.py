
t = list(s)
t.sort()
s = ''.join(t)
s = input()

if (len(s) % 2 == 0) and (s[0] in 'RUD') and (s[-1] in 'RUD'):
elif (len(s) % 2 != 0) and (s[0] in 'RUD') and (s[-1] in 'RUD'):
    print('No')
    print('Yes')
else:
    print('No')
