

import sys

[X,Y] = [int(i) for i in sys.stdin.readline().split()]

if Y == 1:
    print "IMPOSSIBLE"
elif X % (Y - 1) == 0:
    print X / (Y - 1)
else:
    print "ALL GOOD"
