
import sys

b, k, g = map(int, input().split())
print(int(b / g) + (1 if b % g > 0 else 0))
