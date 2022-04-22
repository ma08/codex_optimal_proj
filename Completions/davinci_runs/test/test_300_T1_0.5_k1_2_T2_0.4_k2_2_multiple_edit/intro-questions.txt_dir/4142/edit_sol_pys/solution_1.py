

s = input()

if (len(s) % 2 == 0) and (s[0] in 'RUD') and (s[-1] in 'LUD') and (s.count('R') == s.count('L')) and (s.count('U') == s.count('D')):
    print('Yes')
else:
    print('No')
