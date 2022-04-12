
import sys

#input
x, t = map(int, sys.stdin.readline().rstrip().split())

#calc
if t <= x - t: # tがx-t以下ならば、tを引くだけでOK
    ans = x - 2*t
else: # tがx-tより大きければ、tを引いて2tを足す
    ans = 2*t - x

#output
print(ans)
