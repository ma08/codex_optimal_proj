

# My Answer

s = input()

if s[0] == 'A' and s[2:len(s) - 1].count('C') == 1:
    for i in range(1, len(s)):
        if i != 2 and s[i] not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'):
            print('WA')
            exit()
    print('AC')
else:
    print('WA')

# Best Answer

s = input()

if s[0] == 'A' and s[2:len(s) - 1].count('C') == 1 and s[1:].islower():
    print('AC')
else:
    print('WA')
