
import math

for _ in range(int(input())):
    a, b, c = map(float, input().split())
    print(math.ceil(min(abs(a - b) + abs(a - c) + abs(b - c), abs(a - b - 1) + abs(a - c) + abs(b - c - 1), abs(a - b) + abs(a - c - 1) + abs(b - c - 1), abs(a - b - 1) + abs(a - c - 1) + abs(b - c))))
