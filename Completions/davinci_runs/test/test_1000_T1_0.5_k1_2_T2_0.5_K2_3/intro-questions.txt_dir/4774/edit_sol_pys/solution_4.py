
import sys
lines = sys.stdin.readlines()

a, b, c, d = [int(x) for x in lines[0].split()]

valid = []

# a + b = c + d
if a + b == c + d:
    valid.append('{} + {} = {} + {}'.format(a, b, c, d))

# a - b = c - d
if a - b == c - d:
    valid.append('{} - {} = {} - {}'.format(a, b, c, d))

# a * b = c * d
if a * b == c * d:
    valid.append('{} * {} = {} * {}'.format(a, b, c, d))

# a / b = c / d
if b != 0 and d != 0 and a / b == c / d:
    valid.append('{} / {} = {} / {}'.format(a, b, c, d))

if len(valid) > 0:
    print('\n'.join(sorted(valid)))
else:
    print('no solution')
