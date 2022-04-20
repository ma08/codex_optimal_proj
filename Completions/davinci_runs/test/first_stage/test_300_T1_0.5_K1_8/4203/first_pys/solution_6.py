

s = input()

if s[0] == 'A' and 'C' in s[2:-1] and s[2:-1].count('C') == 1:
    print('AC')
else:
    print('WA')