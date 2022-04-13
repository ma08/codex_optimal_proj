
import sys
l, r = map(int, input().split())  # map returns an iterator

if l == 0 and r == 0:
    sys.stdout.write('Not a moose')
elif l == r:
    sys.stdout.write('Even {}'.format(l + r))
else:
    sys.stdout.write('Odd {}'.format(max(l, r) * 2))
