

# My Answer

s = input()

if s[0] == 'A' and s[2:len(s)-1].count('C') == 1:
    for i in range(1, len(s)):
        if i != 2 and s[i] not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'):
            print('WA')
            exit()
    print('AC')
else:
    print('WA')

# Best Answer

s = input()

if s[0] == 'A' and s[2:len(s)-1].count('C') == 1 and s[1:].islower():
    print('AC')
else:
    print('WA')
