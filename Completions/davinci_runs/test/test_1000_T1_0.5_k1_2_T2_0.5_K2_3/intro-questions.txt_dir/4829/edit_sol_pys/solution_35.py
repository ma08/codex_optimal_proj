
#-----main-----

l, r = map(int, input().split())

if l == r and l != 0:
    print('Even ' + str(l + r))
elif l != r:
    print('Odd ' + str(max(l, r) * 2))
else:
    print('Not a moose')
