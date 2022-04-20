

import sys

N, A, B = map(int, sys.stdin.readline().split())

print(N // (A + B) * A + min(N % (A + B), A))