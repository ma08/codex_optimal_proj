
import sys

for s in sys.stdin:
    if s[-1] == 'y':
        print(s[:-1] + 'ies')
    else:
        print(s + 's')
