
import sys
 
N = int(sys.stdin.readline())

for i in range(N + 1, 1000000):
    if len(set(list(str(i)))) == 1: print(i); break
