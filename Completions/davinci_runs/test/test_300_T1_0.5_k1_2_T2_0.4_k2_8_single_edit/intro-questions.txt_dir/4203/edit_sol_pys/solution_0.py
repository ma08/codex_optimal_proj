

s = list(str(input()))

if s[0] != 'A':
    print('WA')
    exit()

if s[2:-1].count('C') != 1:
    print('WA')
    exit()

for i in range(2, len(s)-1):
    if s[i] == 'C':
        continue
    elif s[i].islower():
        continue
    else:
        print('WA')
        exit()
    print('AC')
