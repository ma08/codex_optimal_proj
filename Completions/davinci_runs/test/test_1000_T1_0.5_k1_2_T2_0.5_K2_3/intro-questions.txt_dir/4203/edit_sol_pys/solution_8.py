
s = input()

if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1].islower():
    for i in range(2, len(s)):
        if s[i] == 'C':
            continue
        elif s[i].islower():
            continue
        else:
            print('WA')
            break
    print('AC')
else:
    print('WA')
