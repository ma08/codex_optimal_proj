import math

A,B,C = map(int, input().split())

print(math.floor(B/A) if B/A <= C else C)
