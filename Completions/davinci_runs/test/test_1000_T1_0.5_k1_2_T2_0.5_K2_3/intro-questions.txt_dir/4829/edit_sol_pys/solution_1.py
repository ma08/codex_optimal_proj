

l, r = map(int, input().split())

if l == 0 and r == 0:
    print('Not a moose')
elif l == r:
    print('Even {}'.format(l + r))
else:
# fix spelling mistakes
    print('Odd {}'.format(max(l, r) * 2))
