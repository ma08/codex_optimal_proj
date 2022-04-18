
l, r = map(int, input().split())

if l == 0 and r == 0:
    print('Not a moose')
elif l == r:
    print('Even {}'.format(2 * l))
else:
    print('Odd {}'.format(max(l, r) * 2))
