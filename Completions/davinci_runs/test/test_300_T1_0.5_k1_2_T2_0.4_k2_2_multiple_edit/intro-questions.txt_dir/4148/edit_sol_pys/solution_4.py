
import sys
import math

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

for s in S:
    print(chr(ord(s) + N) if ord(s) + N <= ord('Z') else chr(ord(s) + N - ord('Z') + ord('A') - 1), end='')

# ord() : character to ASCII
# chr() : ASCII to character
