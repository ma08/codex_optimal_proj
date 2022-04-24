
import math
from sys import stdin

# Read from standard input
N, A, B = map(int, stdin.readline().split())

# if N%(A+B) == 0:
#     print(math.floor(N/(A+B))*A)
# elif N%(A+B) >= A:
#     print(math.floor(N/(A+B))*A + A)
# else:
#     print(math.floor(N/(A+B))*A + N%(A+B))

print(min(A, B) * math.floor(N/(A+B)) + min(N%(A+B), A))
