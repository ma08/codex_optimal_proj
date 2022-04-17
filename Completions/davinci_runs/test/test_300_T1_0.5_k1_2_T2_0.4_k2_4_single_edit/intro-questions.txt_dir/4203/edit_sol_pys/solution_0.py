
s = str(input())

if s[0] == 'A' and s[2:-1].count('C') == 1 and s[2:-1].islower():
    print('AC')
    exit()
print('WA')
