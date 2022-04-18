

import sys

[X,Y] = [int(i) for i in sys.stdin.readline().split()]

if Y == 1:
    print "IMPOSSIBLE" + "\n"
elif X % (Y - 1) == 0:
    print str(X / (Y - 1)) + "\n"
else:
    print "ALL GOOD!" + "\n"
