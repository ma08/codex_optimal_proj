

s = input()

if (len(s) % 2 == 0) and (s[0] in 'RUD') and (s[-1] in 'LUD') and (s.count('L') == s.count('R')):
    print('Yes')
else:
    print('No')
