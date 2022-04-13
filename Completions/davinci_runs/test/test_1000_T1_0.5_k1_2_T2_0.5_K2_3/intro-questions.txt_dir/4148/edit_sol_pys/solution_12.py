
# read input
import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

for s in S:
    print(chr(ord(s) + N) if ord(s) + N <= ord('z') else chr(ord(s) + N - ord('z') + ord('a') - 1), end='')

# ord() : character to integer
# chr() : integer to character
