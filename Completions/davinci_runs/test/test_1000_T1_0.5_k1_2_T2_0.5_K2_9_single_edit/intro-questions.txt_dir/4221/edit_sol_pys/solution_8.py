
import sys
for line in sys.stdin:
    s = line.strip()
    if s[-1] == 's':
        print(s + 'es')
    else:
        print(s + 's')
