
import sys
N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()
for s in S:
    print(chr(ord(s) + N) if ord(s) + N <= ord('Z') else chr(ord(s) + N - ord('Z') + ord('A') - 1), end='')


# ord() : character to integer
# chr() : integer to character
