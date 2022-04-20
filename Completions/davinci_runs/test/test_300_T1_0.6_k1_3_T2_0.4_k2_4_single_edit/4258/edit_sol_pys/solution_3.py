
import math

a, b, c = map(int, input().split())

ans = math.floor(c / a) * b
print(int(ans))
