
import sys
import collections

n = int(sys.stdin.readline())
verdicts = sys.stdin.read().split()
counts = collections.Counter(verdicts)
for verdict, count in counts.items():
    print(verdict, "x", count)
