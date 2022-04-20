

s = input()

if s[0] == 'A' and s[2:len(s)-1].count('C') == 1:
    for i in range(len(s)):
        if i != 0 and i != 2 and s[i] != s[i].lower():
            print('WA')
            break
    else:
        print('AC')
else:
    print('WA')