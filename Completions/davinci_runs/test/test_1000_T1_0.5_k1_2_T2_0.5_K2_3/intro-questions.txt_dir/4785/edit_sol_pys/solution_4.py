import sys
for line in sys.stdin:
    if 'ss' in line:
        print('hiss')
    else:
        print('no hiss')
