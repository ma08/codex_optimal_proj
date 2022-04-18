

s = input()
if s[0] == 'A' and s[2:-1].count('C') == 1:
    s = s[1:]
    s = s.replace('C', '')
    if s.islower():
        print('AC')
    else:
        print('WA')
else:
    print('WA')
