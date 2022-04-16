

s = input()

if (len(s) % 2 == 0) and (s[0] in 'RL') and (s[-1] in 'RL'):
    print('Yes')
else:
    print('No')
