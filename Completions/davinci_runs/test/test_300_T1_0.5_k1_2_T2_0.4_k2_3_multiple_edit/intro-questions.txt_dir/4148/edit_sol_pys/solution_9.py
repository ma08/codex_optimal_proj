import sys


def solve(s):
    return chr(ord(s) + N) if ord(s) + N <= ord('Z') else chr(ord(s) + N - ord('Z') + ord('A') - 1)


N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

print(''.join(map(solve, S)))

# ord() : character to integer
# chr() : integer to character
