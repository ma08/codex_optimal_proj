

s = str(input())

if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1].islower() and s[-1].islower() and s[2:-1].islower():
    for i in range(2, len(s)-1):
        if s[i] == 'C':
            continue
        else:
            print('AC')
            exit(0)
    print('AC')
else:
    print('WA')
