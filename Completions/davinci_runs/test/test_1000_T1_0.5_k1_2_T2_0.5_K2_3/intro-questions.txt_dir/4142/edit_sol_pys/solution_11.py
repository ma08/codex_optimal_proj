

s = input()

if (len(s) % 2 == 0) and (s[0] in 'R' or 'U' or 'D') and (s[-1] in 'L' or 'U' or 'D'):
    print('Yes')
else:
    print('No')
