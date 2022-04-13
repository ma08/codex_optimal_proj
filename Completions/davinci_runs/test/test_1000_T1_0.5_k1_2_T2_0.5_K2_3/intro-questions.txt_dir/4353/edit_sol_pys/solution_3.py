import sys

for s in sys.stdin:
    s = s.replace(',', ' ')
    s = s.replace('.', ' ')

    print(s)
