# coding: utf-8

N = input()

if N[-1] == '7':
    print('Yes')
elif N[-2] == '7':
    print('Yes')
elif N[0] == '7':
    print('Yes')
else:
    print('No')
