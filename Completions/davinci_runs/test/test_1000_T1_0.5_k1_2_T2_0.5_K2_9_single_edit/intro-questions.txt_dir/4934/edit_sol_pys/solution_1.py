

import math

h, v = map(float, input().split())

print(math.ceil(h / math.sin(math.radians(v))))
