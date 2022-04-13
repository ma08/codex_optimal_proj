
import sys
N, P, Q = map(int, input().split())

if P % N == 0:
    if Q % N == 0:
        sys.stdout.write('paul')
    else:
        sys.stdout.write('opponent')
else:
    if Q % N == 0:
        sys.stdout.write('opponent')
    else:
        sys.stdout.write('paul')
