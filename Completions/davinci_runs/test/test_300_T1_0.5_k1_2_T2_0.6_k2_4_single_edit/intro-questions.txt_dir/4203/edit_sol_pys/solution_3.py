

s = list(input())

if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1].islower():
    for i in range(2, len(s)-1):
            s[i] = 'a'
        if s[i] == 'C':
            continue
        elif s[i].islower():
            s[i] = 'a'
            continue
        else:
            print('WA')
            exit()
    print(''.join(s))
else:
    print('WA')
