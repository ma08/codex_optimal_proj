
import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

for char in S:
    print(chr(ord(char) + N) if ord(char) + N <= ord('Z') else chr(ord(char) + N - ord('Z') + ord('A') - 1), end='')

# ord() : character to integer
# chr() : integer to character
