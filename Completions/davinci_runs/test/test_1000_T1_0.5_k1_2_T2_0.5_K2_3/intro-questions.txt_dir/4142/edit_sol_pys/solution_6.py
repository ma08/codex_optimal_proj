

s = input('Введите строку: ')

if (len(s) % 2 == 0) and (s[0] in 'UD') and (s[-1] in 'UD') and (s.count('U') == s.count('D')):
    print('Yes')
else:
    print('No')
