
s = str(input()) # 入力

if s[0] == 'A' and s[2:-1].count('C') == 1:
    for i in range(2, len(s)-1):
        if s[i] == 'C':
            continue
        elif s[i].islower():
            continue
        else:
            print('WA')
            exit()
    print('AC')
else:
    print('WA')
