
import math

a, b, x = map(int, input().split())

print(math.floor(b/x) - math.floor((a-1)/x))
