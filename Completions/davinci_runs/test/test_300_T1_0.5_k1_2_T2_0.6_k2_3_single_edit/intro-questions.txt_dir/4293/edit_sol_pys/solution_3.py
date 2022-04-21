
import sys

try:
    P, Q, R = map(int, input().split())
except EOFError:
    sys.exit()

print(min(P+Q, Q+R, R+P))
