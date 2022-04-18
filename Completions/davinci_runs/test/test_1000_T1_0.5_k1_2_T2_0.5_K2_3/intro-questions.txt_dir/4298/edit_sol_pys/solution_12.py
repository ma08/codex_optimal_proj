
import sys
N, D = map(int, input().split())
if N == 0 and D == 0:
    sys.exit()
else:
    print((N+D*2)//(D*2+1))
