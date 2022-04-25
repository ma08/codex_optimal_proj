
s = input()

if len(s) % 2 == 0:
    if s[0::2] == 'RUD' * (len(s) // 2) and s[1::2] == 'LUD' * (len(s) // 2):
        print('Yes')
    else:
        print('No')
else:
    print('No')
