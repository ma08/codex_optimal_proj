
import math
import sys

N, D = map(int, sys.stdin.readline().split())

print(math.ceil(N/(2*D+1)))
