
import math
a, b = map(float, input().split())
print(int(round(a / math.sin(math.radians(b)))))
